import './commands'

function loginViaAAD(username, password) {
    cy.visit('/auth')
    cy.getBySel('signIn').click()
  
    // Login to your AAD tenant.
    cy.origin(
      'login.microsoftonline.com',
      {
        args: {
          username,
        },
      },
      ({ username }) => {
        cy.get('input[type="email"]').type(username, {
          log: false,
        })
        cy.get('input[type="submit"]').click()
      }
    )
  
    // depending on the user and how they are registered with Microsoft,
    // the origin may go to live.com
    cy.origin(
      'login.live.com',
      {
        args: {
          password,
        },
      },
      ({ password }) => {
        cy.get('input[type="password"]').type(password, {
          log: false,
        })
        cy.get('input[type="submit"]').click()
        cy.get('#idBtn_Back').click()
      }
    )
  
    // Ensure Microsoft has redirected us back to the sample app with our logged in user.
    cy.url().should('equal', '/')
    cy.get('#welcome-div').should(
      'contain',
      `Welcome `
    )
}
  
Cypress.Commands.add('loginToAAD', (username, password) => {
  cy.session(
    `aad-${username}`,
    () => {
      const log = Cypress.log({
        displayName: 'Azure Active Directory Login',
        message: [`🔐 Authenticating | ${username}`],
        // @ts-ignore
        autoEnd: false,
      })

      log.snapshot('before')

      loginViaAAD(username, password)

      log.snapshot('after')
      log.end()
    },
    {
      validate: () => {
        // this is a very basic form of session validation for this demo.
        // depending on your needs, something more verbose might be needed
        cy.visit('/')
        cy.get('#welcome-div').should(
          'contain',
          `Welcome ${Cypress.env('aad_username')}!`
        )
      },
    }
  )
})
