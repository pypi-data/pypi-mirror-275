import fsspec

from interlinked import provide, default_workflow, depend

config_dev = {
    "dataset-ssh-{filename}": {
        "url": "ssh://hal2/home/bertrand.chenal/{filename}",
        "type": "csv",  # parquet
    },
    "dataset-local-{filename}": {
        "url": "file://{filename}",
    },
    "ts-{class}-{site_id}-{name}": {
        "url": "file://{class}-{inverter_id}/{name}.csv",
    },
    "ts-site-123-{name}": {
        "url": "file://...",
    },
    "ts-belpex-{date}": {
        "url": "file://{inverter_id}/{name}.csv",
    },
}

config_prod = {
    "dataset-ssh-{filename}": {
        "url": "ssh://hal2/home/bertrand.chenal/{filename}",
        "type": "csv",  # parquet
    },
    "dataset-local-{filename}": {
        "url": "s3://{filename}",
    },
    "ts-{class}-{site_id}-{name}": {
        "url": "s3://{class}-{inverter_id}/{name}.csv",
    },
    "ts-site-123-{name}": {
        "url": "s3://...",
    },
    "ts-belpex-{date}": {
        "url": "s3://{inverter_id}/{name}.csv",
    },
}


def data_fn():
    ...
    for pattern, cfg in config.items():
        provide(pattern)(data_fn)


@provide("ts-belpex-{date}")
@provide("ts-{class}-{item_id}-{name}")
def fsspec_source(**kw):
    # print(kw)
    with fsspec.open(**kwl) as fh:
        return fh.read()


@depend(content="ts-inverter-{inverter_id}-conso")
@provide("transform-hello")
def transform(content):
    return len(content)


if __name__ == "__main__":
    wkf = default_workflow.config(config)
    # res = wkf.run("dataset-ssh-hello.txt", config=config)
    # print(res)

    # res = wkf.run("dataset-local-setup.py", config=config)
    # print(res)

    run("transform-hello")
