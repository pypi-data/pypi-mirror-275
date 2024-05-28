use std::sync::Arc;

use once_cell::sync::Lazy;

use frtb_engine::prelude::FRTBDataSet;
use ultibi::{
    datasource::SourceVariant,
    new::NewSourcedDataSet,
    prelude::{read_toml2, DataSet, DataSourceConfig},
    ComputeRequest, IntoLazy,
};

use ultibi::polars::prelude::{col, Float64Type, IndexOrder};

pub static LAZY_DASET: Lazy<Arc<FRTBDataSet>> = Lazy::new(|| {
    let conf_path = r"data/frtb/datasource_config.toml";
    let conf = read_toml2::<DataSourceConfig>(conf_path)
        .expect("Can not proceed without valid Data Set Up"); //Unrecovarable error
    let mut data: FRTBDataSet = FRTBDataSet::from_config(conf);
    data.validate_frame(None, 0).expect("failed to validate");
    //comment out if testing Scanning
    data.prepare().expect("Failed to prepare");
    std::sync::Arc::new(data)
});

pub static LAZY_SCAN_DASET: Lazy<Arc<FRTBDataSet>> = Lazy::new(|| {
    let conf_path = r"data/frtb/datasource_config.toml";
    let mut conf = read_toml2::<DataSourceConfig>(conf_path)
        .expect("Can not proceed without valid Data Set Up"); //Unrecovarable error
                                                              //change DataSource to Scan for this test
    *conf.get_source_type_mut() = SourceVariant::Scan;
    let data: FRTBDataSet = FRTBDataSet::from_config(conf);
    data.validate_frame(None, 0).expect("failed to validate");
    std::sync::Arc::new(data)
});

#[ignore]
#[allow(dead_code)]
pub fn assert_results(req: &str, expected_sum: f64, epsilon: Option<f64>) {
    let ep = if let Some(e) = epsilon { e } else { 1e-7 };
    let data_req = serde_json::from_str::<ComputeRequest>(req).expect("Could not parse request");
    let excl = if let ComputeRequest::Aggregation(agg_req) = data_req.clone() {
        agg_req.group_by().clone()
    } else {
        unreachable!()
    };
    //let excl = data_req.group_by().clone();
    let a = LAZY_DASET.as_ref();

    let res = a
        .compute(data_req)
        .expect("Error while calculating results");

    let res_numeric = res
        .lazy()
        .select([col("*").exclude(excl)])
        .collect()
        .expect("Could not remove column");
    let res_arr = res_numeric
        .to_ndarray::<Float64Type>(IndexOrder::Fortran)
        .expect("Could not convert result to nd_array");
    // Slightly naive, but we assume if the sum is equivallent then the result is accurate
    dbg!(res_arr.sum());
    dbg!(expected_sum);
    assert!((res_arr.sum() / expected_sum - 1.0).abs() < ep);
}

#[ignore]
#[allow(dead_code)]
pub fn assert_results_scan(req: &str, expected_sum: f64, epsilon: Option<f64>) {
    let ep = if let Some(e) = epsilon { e } else { 1e-7 };
    let data_req = serde_json::from_str::<ComputeRequest>(req).expect("Could not parse request");
    let excl = if let ComputeRequest::Aggregation(agg_req) = data_req.clone() {
        agg_req.group_by().clone()
    } else {
        unreachable!()
    };

    let a = LAZY_SCAN_DASET.as_ref();
    let res = a
        .compute(data_req)
        .expect("Error while calculating results");
    let res_numeric = res
        .lazy()
        .select([col("*").exclude(excl)])
        .collect()
        .expect("Could not remove column");
    let res_arr = res_numeric
        .to_ndarray::<Float64Type>(IndexOrder::Fortran)
        .expect("Could not convert result to nd_array");
    // Slightly naive, but we assume if the sum is equivallent then the result is accurate
    dbg!(res_arr.sum());
    dbg!(expected_sum);
    assert!((res_arr.sum() / expected_sum - 1.0).abs() < ep);
}
