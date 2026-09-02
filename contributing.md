
Generating a CHANGELOG.

We using 
```
git-chglog -o CHANGELOG.md
```

### Commits

We try to follow the [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) approach, which makes it easier to generate a changelog.

The structure of the commits should be
```
type: commit msg
```

The commit types that will be included and grouped in the CHANGELOG are:

spec: "𝌭 Model changes"
app: "👷‍♀️ Application changes"
tool: "⚒️ Tooling"
fix:  "🐛 Bug Fixes"
docs: "📚 Documentation"
req: "📄 Planning requirement"
need: "🎯 Need"
guidance: "🧭 Guidance"

### Tags

We use tags to group changes.

We create new tags with 
```
git tag -a v0.1.1 -m "a description"
```
