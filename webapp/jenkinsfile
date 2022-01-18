pipeline {
    agent any

    stages {
        stage ('build') {
            steps{
                sh 'cd /var/lib/jenkins/workspace/MultiBranchPipeline-Job_main/webapp'
                sh 'docker-compose -f /var/lib/jenkins/workspace/MultiBranchPipeline-Job_main/webapp/docker-compose.yml up --build'
            }
        }

        stage ('test') {
            steps{
                echo 'Test stage executed.'
            }
        }

        stage ('deploy') {
            steps{
                echo 'Deploy stage executed.'
            }
        }
    }
}