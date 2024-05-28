use ultibi_core::{
    polars::{
        prelude::{DataType, IdxSize, IntoLazy, NamedFrom, QuantileInterpolOptions, Schema},
        series::Series,
    },
    DataFrame, PolarsResult,
};

/// We override Polars' describe function to better fit our needs
pub fn describe(df: DataFrame, percentiles: Option<&[f64]>) -> PolarsResult<DataFrame> {
    fn describe_cast(df: &DataFrame, original_schema: &Schema) -> PolarsResult<DataFrame> {
        let columns = df
            .get_columns()
            .iter()
            .zip(original_schema.iter_dtypes())
            .map(|(s, original_dt)| {
                if original_dt.is_numeric() | matches!(original_dt, DataType::Boolean) {
                    s.cast(&DataType::Float64)
                }
                // for dates, strings, etc, we cast to string so that all
                // statistics can be shown
                else {
                    s.cast(&DataType::String)
                }
            })
            .collect::<PolarsResult<Vec<Series>>>()?;

        DataFrame::new(columns)
    }

    fn count(df: &DataFrame) -> DataFrame {
        let columns = df
            .get_columns()
            .iter()
            .map(|s| Series::new(s.name(), [s.len() as IdxSize]))
            .collect();
        unsafe { DataFrame::new_no_checks(columns) }
    }

    let percentiles = percentiles.unwrap_or(&[0.25, 0.5, 0.75]);

    let mut headers: Vec<String> = vec![
        "null_count".to_string(),
        "sum".to_string(),
        "mean".to_string(),
        "std".to_string(),
        "min".to_string(),
        "max".to_string(),
    ];

    let original_schema = df.schema();

    let mut tmp: Vec<DataFrame> = vec![
        describe_cast(&df.null_count(), &original_schema)?,
        describe_cast(&df.clone().lazy().sum().collect()?, &original_schema)?,
        describe_cast(&df.clone().lazy().mean().collect()?, &original_schema)?,
        describe_cast(&df.clone().lazy().std(1).collect()?, &original_schema)?,
        describe_cast(&df.clone().lazy().min().collect()?, &original_schema)?,
        describe_cast(&df.clone().lazy().max().collect()?, &original_schema)?,
    ];

    for p in percentiles {
        tmp.push(describe_cast(
            &df.clone()
                .lazy()
                .quantile((*p).into(), QuantileInterpolOptions::Linear)
                .collect()?,
            &original_schema,
        )?);
        headers.push(format!("{}%", *p * 100.0));
    }

    // Keep order same as pandas
    //tmp.push(describe_cast(&df.max(), &original_schema)?);
    let mut res = describe_cast(&count(&df), &original_schema)?;
    let mut header = vec!["count".to_string()];
    header.extend(headers);

    for d in tmp {
        res.vstack_mut(&d)?;
    }

    res.insert_column(0, Series::new("describe", header))?;

    Ok(res)
}
