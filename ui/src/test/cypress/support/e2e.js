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
  
    cy.url().should('contain', '/auth')
    cy.getBySel('logOut').should('be.visible')
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
        cy.visit('/auth')
        cy.getBySel('accountsAmount').should('have.text', '1')
      },
    }
  )
})