# Upload file to AnonFiles

This GitHub action allows you to upload a file to anonfiles.com.

## Usage

```yml
- name: Upload README.md
  uses: Siege-Wizard/anonfiles-upload@1.0.0
  with:
    file: README:md
  env:
    ANONFILES_TOKEN: ${{ secrets.ANONFILES_TOKEN }}
```

**Required Parameters:**

- `file`: The file that should be uploaded to anonfiles.com.

**Environmetal variables:**

- `ANONFILES_TOKEN`: If provided, the file will be uploaded to the 
  corresponding account instead.

### Outputs

- `url`: Url of the uploaded file.
