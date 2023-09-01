# Some examples of data models in Pydantic v1 

## Usage 

Activate the virtual environment, 

    $ poetry shell 

And install the relevant packages 

    (v1-py11)$ poetry install 

Now you can play around with the different implementations:

1.  Validation of a data model 

        (v1-py11)$ python model.py

2. Time pydantic's work in action 

        (v1-py11)$ python validate_and_time.py

3. Test pydantic with a mypy-integration 

        (v1-py11)$ mypy *.py

4. See how `pydantic`+`fastapi`+`uvicorn` looks like

        (v1-py11)$ uvicorn fast_api_example:app --reload

5. Investigate how to use `Field` with restrictions on the value of the variable 

        (v1-py11)$ python fast_api_example.py