# AWS EC2 snapshot
EC2 snapshot with python


## About
 This project is using boto3 to manage EC2 snapshot

## Configuring

Configure AWS CLI profile with 'shotty' name

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <subcommand> <--Project=PROJECT>`

*command* is instances, volumes or snapshots

*subcommand* depends on the command

*project* is optional

You can download my package from
`pip3 install https://pythoncommands.s3.amazonaws.com/aws_ec2_snapshot-0.1-py3-none-any.whl`

Also you can below commands 

```
shotty instances list
shotty instances start
shotty instances stop

shotty --help

shotty instances --help
```

#### PROJECT is a value of tag which given to EC2  and it's Key is 'Project'
`shotty instances list --Project=PROJECT`

