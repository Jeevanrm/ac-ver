pipeline{
    agent none
    environment{
            TEST="test value1"
            TEST1="test value 2"
              }
    stages{
        stage('Build'){
            agent {
                   label "slave1"
                   }
            steps{ 
                    sh ''' sleep 5
                    echo "$TEST" 
                '''
            }
            }
        stage('test'){
            agent any

             steps{
                   scripts{
                    echo "${env.TEST}"
                    }
            }
           
            }
        }
    }

