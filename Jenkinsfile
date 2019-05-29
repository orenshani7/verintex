pipeline {
	agent any

	node {
		checkout scm
		}

	stages {
		stage('verify') {
			steps {
				sh 'checkmd5.sh'
				}
			}

		stage('test') {
			steps {
				sh 'python3 gethw.py > gethw.json'
				sh 'json_pp < gethw.json > /dev/null'
				}
			}
		}	
				
	}
