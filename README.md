
## myman: Sequence of posts by Kevin Kruse starting with 'My man ...'

[![CI](https://github.com/eddelbuettel/myman-py/workflows/ci/badge.svg)](https://github.com/eddelbuettel/myman-py/actions?query=workflow%3Aci)
[![License](https://img.shields.io/badge/license-GPL%20%28%3E=%202%29-brightgreen.svg?style=flat)](https://opensource.org/license/gpl-2.0) 
[![pypi](https://img.shields.io/pypi/v/myman?color=3776ab)](https://pypi.org/project/myman/)
[![Last Commit](https://img.shields.io/github/last-commit/eddelbuettel/myman-py)](https://github.com/eddelbuettel/myman-py)


### Motivation

Starting on the afternoon of July 17, 2026, and lasting for one initial week, Kevin Kruse fired off
an astonishing array of over six hundred ninety eight BlueSky replies to [an initial post of
his][postone] featuring a certain government figure. On August 12, 2026, a second wave started [with
this post][posttwo] aiming at another government figure. (There were also two stray posts from the
interim period.) This was followed on August 17, 2026, with another series starting with [this
post][postthree]. A fourth wave started on August 27, 2026, with [this post][postfour].  A fifth
wave started on August 30, 2026, with [this post][postfive]. A sixth wave started on September 4,
2026 with [this post][postsix]. The total now stands at one thousand three hundred ninety four
posts.

All posts start with "My man ..." and make for excellent input to a `fortunes`-like package. So this
small package obliges and offers a random draw each time its `myman()` function is called.  This
Python package benefits from the corresponding [R package][rpkg] and uses the csv file created and
packaged there.

The Python package is equivalent to the R in all aspects but one: each call will only return one
post. 

### Example

The simple file `main.py` illustrates three calling examples with (numeric) index, target, or
topical index.

```sh
$ ./main.py 
My man looks like Pat Boone being tased.
         -- about Stephen Miller on 2026-07-16

My man looks like a superhero whose power is Bryl Cream.
         -- about Scott Bessent on 2026-08-31

My man looks like he's asked the maitre'd to remove a party of \
four he finds visually unpleasant.
         -- about Scott Bessent on 2026-08-30

```

### Author

Dirk Eddelbuettel

### License

GPL (>= 2)

[postone]: https://bsky.app/profile/did:plc:cnpe7qvcyjrhm6w7w7e4atur/post/3mqum4mxsuk2g
[posttwo]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3mstvbjpagca2
[postthree]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3mtcpiw7gi22j
[postfour]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3mu3pugs2yk2f
[postfive]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3mudbzy5ksk25
[postsix]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3muparqtdkk2w

[rpkg]: https://github.com/eddelbuettel/myman
