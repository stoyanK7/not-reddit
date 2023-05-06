workspace {

    model {
        notredditUser = person "Not-reddit User" {
            tags "Microsoft Azure - Users" "person"
        }

        notredditSystem = softwareSystem "Not-reddit"{
            tags "service" "notreddit"
            spApplication = container "not-reddit Single Page Application" {
                tags "service" "spa"
            }
            gateway = container "API Gateway" {
                tags "service" "nginx"
            }

            group "Authentication Service" {
                authApi = container "Authentication API" {
                    tags "service" "fastapi"
                }
            }

            group "User Service" {
                userApi = container "User API" {
                    tags "service" "fastapi"
                }
                userDb = container "User Database" {
                    tags "postgresql"
                }
            }

            group "Post Service" {
                postApi = container "Post API" {
                    tags "service" "fastapi"
                }
                postDb = container "Post Database" {
                    tags "postgresql"
                }
            }

            group "Comment Service" {
                commentApi = container "Comment API" {
                    tags "service" "fastapi"
                }
                commentDb = container "Comment Database" {
                    tags "postgresql"
                }
            }

            group "Vote Service" {
                voteApi = container "Vote API" {
                    tags "service" "fastapi"
                }
                voteDb = container "Vote Database" {
                    tags "postgresql"
                }
            }

            group "Email Service" {
                emailScript = container "Email Script" {
                    tags "service" "python"
                }
            }

            eventBus = container "Event Bus" {
                tags "service" "rabbitmq"
                userRegisteredEvent = component "User Registered Event" {
                    tags "event"
                }
                postCreatedEvent = component "Post Created Event" {
                    tags "event"
                }
                commentCreatedEvent = component "Comment Created Event" {
                    tags "event"
                }
                postVoteCastedEvent = component "Post Vote Casted Event" {
                    tags "event"
                }
                commentVoteCastedEvent = component "Comment Vote Casted Event" {
                    tags "event"
                }
            }
        }

        azureAdSystem = softwareSystem "Microsoft Azure Active Directory" {
            tags "Microsoft Azure - Azure Active Directory" "azureActiveDirectory"
        }

        azureBlobStorage = softwareSystem "Microsoft Azure Blob Storage" {
            tags "Microsoft Azure - Blob Page" "azureBlobStorage"
        }

        azureEmailCommunicationService = softwareSystem "Microsoft Azure Email Communication Service" {
            tags "Microsoft Azure - Azure Communication Services" "azureEmailCommunicationService"
        }

        notredditUser -> spApplication "Uses"
        notredditUser -> azureAdSystem "Authenticates with"

        spApplication -> gateway "Uses"
        spApplication -> azureAdSystem "Gets access token from"

        gateway -> authApi "Routes to"
        gateway -> userApi "Routes to"
        gateway -> postApi "Routes to"
        gateway -> commentApi "Routes to"
        gateway -> voteApi "Routes to"

        authApi -> azureAdSystem "Ensures access token is valid with"

        userApi -> eventBus "Communicates with"
        userApi -> userRegisteredEvent "Publishes"
        userApi -> userDb "Stores information in"

        postApi -> azureBlobStorage "Stores media in"
        postApi -> eventBus "Communicates with"
        postApi -> postDb "Stores information in"
        postApi -> postCreatedEvent "Publishes"
        postApi -> userRegisteredEvent "Subscribes to"
        postApi -> postVoteCastedEvent "Subscribes to"

        commentApi -> eventBus "Communicates with"
        commentApi -> postCreatedEvent "Subscribes to"
        commentApi -> userRegisteredEvent "Subscribes to"
        commentApi -> commentDb "Stores information in"
        commentApi -> commentCreatedEvent "Publishes"
        commentApi -> commentVoteCastedEvent "Subscribes to"

        voteApi -> eventBus "Communicates with"
        voteApi -> voteDb "Stores information in"
        voteApi -> userRegisteredEvent "Subscribes to"
        voteApi -> postCreatedEvent "Subscribes to"
        voteApi -> commentCreatedEvent "Subscribes to"
        voteApi -> postVoteCastedEvent "Publishes"
        voteApi -> commentVoteCastedEvent "Publishes"

        emailScript -> azureEmailCommunicationService "Sends emails using"
        emailScript -> eventBus "Subscribes to"
        emailScript -> userRegisteredEvent "Subscribes to"

        azureEmailCommunicationService -> notredditUser "Sends emails to"
    }

    views {
        theme https://static.structurizr.com/themes/microsoft-azure-2023.01.24/theme.json

        systemContext notredditSystem {
            include *
            autolayout
        }

        container notredditSystem {
            include *
        }

        component eventBus {
            include *
        }

        styles {
            element "notreddit" {
                icon img/notreddit.png
                strokeWidth 5
                stroke #808080
            }

            element "service" {
                background #ffffff
                color #363636
                strokeWidth 5
                stroke #808080
            }

            element "fastapi" {
                icon img/fastapi.png
                background #E6F4F3
            }

            element "python" {
                icon img/python.png
                background #AFC4D6
            }

            element "nginx" {
                icon img/nginx.png
                background #FFFAA0
            }

            element "azureBlobStorage" {
                shape Folder
                background #e8fbff
            }

            element "postgresql" {
                shape Cylinder
                background #FFE5E5
                color #363636
                icon img/postgresql.png
                strokeWidth 5
                stroke #808080
            }

            element "azureActiveDirectory" {
                background #e8fbff
            }

            element "azureEmailCommunicationService" {
                background #e0d5f5
            }

            element "person" {
                shape Person
                background #b2e3ed
            }

            element "spa" {
                shape WebBrowser
                background #e8e8e8
                icon img/nextjs.png
            }

            element "rabbitmq" {
                shape Pipe
                background #ffd7a6
                icon img/rabbitmq.png
            }

            element "event" {
                shape Hexagon
                background #dddddd
                strokeWidth 5
                stroke #808080
            }
        }
    }

}
