pipeline{
    agent none
    environment{
            TEST="test value1"
            TEST1="test value 2"
              }
    parameter{
             string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
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
                   script{
                       echo "${params.PERSON}"
                          }
            }
           
            }
        }
    }

