# hack-university-orm
Intro to ORM


## Quick start

```console
# get the repo
git clone git@github.com:hackoregon/hack-university-orm.git
cd hack-university-orm

# create and activate the python virtual environment 
virtualenv .virt
source .virt/bin/activate

# install the python requirements and dependencies
pip install -U pip
pip install -r requirements.txt

# create the database and run migrations
createdb orms
cd orms
python manage.py migrate
```

The `migrate` command will produce output similar to:
```console
Operations to perform:
  Apply all migrations: admin, contenttypes, auth, sessions
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying sessions.0001_initial... OK
```

### Coming back to the project
If you've already installed the dependencies you can activate the virtual environment to jump back in to where you left off.

```console
source .virt/bin/activate
```

### Class Notes
See [Class Notes](class_notes.md)


## License
The MIT License (MIT)
