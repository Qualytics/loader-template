# loader-cookiecutter
A [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating
[Meltano](https://meltano.com/) loaders.

The best way to demonstrate creating your loader structure is with an example.
Below I will initialize the "loader-foobar" project:

Start by installing cookiecutter:
```bash
$ pip install cookiecutter
```

The next command will ask for some input.  Enter the name of your tap:
```bash
$ cookiecutter https://github.com/Qualytics/loader-cookiecutter.git
project_name [e.g. 'loader-json']: loader-foobar
```

For the package_name, I just hit enter since loader_foobar is what I wanted:
```bash
package_name [loader_foobar]:
```

our project now exists. Next integrate with a Meltano project.

## Add to Meltano Project

First create a [Meltano Project](https://meltano.com/docs/getting-started.html#create-your-meltano-project).

Once you have your meltano project initialized, you are ready to add this extractor
as a custom extractor. To do this, run the following in your Meltano Project and
provide the prompted information:

```bash
$ meltano add --custom loader <loader-name>
(namespace): <loader_name>
(pip_url): -e <project-directory-path>
(executable): <loader-name>
(settings): username, password
```

To edit your config variables (settings), edit the meltano.yml file found in your Meltano
project.

Now you can get to work on writing your extractor! See todo's in \_\_init\_\_.py.


See the [Run a data integration (EL) pipeline](https://meltano.com/docs/getting-started.html#install-meltano) section of the Getting Started meltano docs for instructions on running an extractor with your loader
