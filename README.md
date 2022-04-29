# **Solution**
## **Setting Up Virtual Environment And Running Application**
```python
# Bash terminal used for the below commands

# Cloning a local copy of the project in your local machine 
> */technical_interview: git clone https://github.com/robelberhanu/technical_interview.git

# Creating a venv
> */technical_interview: python3.8 -m venv env

# Activating the venv
# Windows
> */technical_interview: source '.\env\Scripts\activate'
# Ubuntu Debian
> */technical_interview: source  env/bin/activate

# Deactivating the venv
> */technical_interview(env): deactivate

## **Installing packages**


# Installing packages used to build the system.
> */technical_interview(env): pip3 install -r requirements.txt



## **Running Appliction**


# XXX: Running entire program
# Do not for get setting up the venv
> */technical_interview(env): uvicorn main:app --reload








