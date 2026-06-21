# Golden Installer Fixtures

These fixtures define expected file lists for real installer end-to-end tests.

They are intentionally small: each fixture records the paths the installer must create for one mode/language/structure combination. The tests install into a temporary repository and compare the actual file tree with these lists.
