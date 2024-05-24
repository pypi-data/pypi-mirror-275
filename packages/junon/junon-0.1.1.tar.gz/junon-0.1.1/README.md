# Junon

## Overview

Junon is a Chatbot-like assistant on your jupyter notebook/lab.

Two types of assistants are built in.

- Data Analytics Assistant
- Writing Assistant

And, You can build your own assistant by using the `junon.assistants` module.

## Getting Started

### Installation

You can install this package from pypi.
```
pip install junon
```

### Setup

Junon uses `OpenAI` API or `Microsoft Azure OpenAI` API to generate text. 

Depending on which one you use, the required environment variables are different.

Please set the environment variables before the activation described below. (You need to set it before activation or importing junon package.)

**OpenAI API**

```
%env OPENAI_API_KEY XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```


**Microsoft Azure OpenAI API**
```
%env AZURE_OPENAI_API_KEY XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%env AZURE_OPENAI_ENDPOINT https://xxxxxxxxxxxxxxxxxxxxxxx.openai.azure.com/
%env AZURE_OPENAI_DEFAULT_MODEL xxxxxx
```

**note** :
`AZURE_OPENAI_DEFAULT_MODEL` is not the model name, but the deployment name of the model deployed on Azure.

### Activation

Run following magic command in your jupyter notebook/lab to activate the assistant you want to use.

Data Analytics Assistant :
```
%load_ext junon.assistants.data_analytics
```

Wrtiting Assistant :
```
%load_ext junon.assistants.writing_assistant
```

### Usage

Junon is Chatbot-like assistant on your jupyter notebook/lab. 

You can use it by sending a message to the assistant.

You can send a message to the assistant by executing the `%%agent` magic command in a code cell of Jupyter Notebook/Lab.

Example:
```
%%agent
Hello, My assistant! 
I want to write a novel. 
Can you help me?
```

The assistant will reply to your message.

### Managment Conversation

You can manage the conversation with the assistant by using some magic commands.

To show the usage of the magic command, execute the following command in a code cell of Jupyter Notebook/Lab.
```
%usage
```

You have to activate the assistant before using the magic command.


## upload to pypi

```
python setup.py sdist bdist_wheel
