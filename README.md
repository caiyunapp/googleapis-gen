# `googleapis-gen`

> [!NOTE]
>
> This package only generated
> [a few proto files](https://github.com/caiyunapp/googleapis-gen/blob/v0.1.2/buf.gen.yaml#L10-L16)
> from the upstream `googleapis` repository. It is not a full copy of the
> `googleapis` repository. Please refer to the upstream repository for the full
> set of proto files.
>
> The generated files are under the `google` namespace, to work with other
> generated codes.

### Install

```bash
pip install googleapis-gen
```

## Background

We have a few projects that depend on the `googleapis` repository in Python.
Unlike Go where people could use
[`google.golang.org/genproto/googleapis`](https://pkg.go.dev/google.golang.org/genproto/googleapis),
Google does not provide a Python package for the `googleapis` repository. And we
only need a few subset of the whole proto files in the `googleapis` repository.
That's why we created this package.

Please be aware that:

- this package **won't** provide full feature like Go's.
- because of the lack of resources, we can only support the latest 2 versions of
  Python.

## LICENSE

- [Apache License 2.0](./LICENSE)
- Upstream:
  [googleapis/googleapis](https://github.com/googleapis/googleapis/blob/master/LICENSE)
  - or a copy: [LICENSE_GOOGLE](./LICENSE_GOOGLE)
