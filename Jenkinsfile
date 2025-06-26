pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo '✅ Cloning the repository...'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 backup_tool.py test.txt "Hello from Jenkins"'
            }
        }
    }
}
