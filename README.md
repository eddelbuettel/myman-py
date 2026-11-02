
## myman: Sequence of posts by Kevin Kruse starting with 'My man ...'

[![CI](https://github.com/eddelbuettel/myman-py/workflows/ci/badge.svg)](https://github.com/eddelbuettel/myman-py/actions?query=workflow%3Aci)
[![License](https://img.shields.io/badge/license-GPL%20%28%3E=%202%29-brightgreen.svg?style=flat)](https://opensource.org/license/gpl-2.0) 
[![pypi](https://img.shields.io/pypi/v/myman?color=3776ab)](https://pypi.org/project/myman/)
[![Last Commit](https://img.shields.io/github/last-commit/eddelbuettel/myman-py)](https://github.com/eddelbuettel/myman-py)


### Motivation

Starting on the afternoon of July 17, 2026, and lasting for one initial week, Kevin Kruse fired off
an astonishing array of over six hundred ninety eight BlueSky replies to [an initial post of
his][postone] featuring a certain government figure. Additional waves followed: [two][posttwo]
(August 12, 2026), [three][postthree] (August 17, 2026), [four][postfour] (August 27, 2026),
[five][postfive] (August 30, 2026), [six][postsix] (September 4, 2026), [seven][postseven]
(September 12, 2026), [eighth][posteight] (Septemer 16, 2026), [nine][postnine] (October 1, 2026),
[ten][postten] (October 4, 2026), [eleven][posteleven] (October 9, 2026), [twelve][posttwelve]
(October 14, 2026), [thirteen][postthirteen] (October 31, 2026). The total
now stands at two thousand two hundred eighty four one posts. 

All posts start with "My man ..." and make for excellent input to a `fortunes`-like package. So this
small package obliges and offers a random draw each time its `myman()` function is called.  This
Python package benefits from the corresponding [R package][rpkg] and uses the csv file created and
packaged there.

The Python package is equivalent to the R in its core aspect but each call will only return one
post. The R package also has two auxiliary functions.

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
[postseven]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3mvdol6xu5k2s
[posteight]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3mvnmq23nw22y
[postnine]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3mwtx2jztkk2g
[postten]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3mx333hlmdc2o
[posteleven]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3mxgzqblov22r
[posttwelve]: https://bsky.app/profile/leftistwonk.bsky.social/post/3mxsfblcuh22d
[postthirteen]: https://bsky.app/profile/kevinmkruse.bsky.social/post/3mz6wwpjpmc2j

[rpkg]: https://github.com/eddelbuettel/myman
