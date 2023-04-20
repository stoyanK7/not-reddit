/// <reference types="cypress" />


describe('Authentication', () => {

    beforeEach(() => {
      cy.loginToAAD(Cypress.env('aad_username'), Cypress.env('aad_password'))
    })

    it('should show logout button and hide signin button', () => {
      cy.visit('/auth')

      cy.getBySel('logOut').should('exist')
      cy.getBySel('signIn').should('not.exist')

    })

    it('should log out', () => {
      cy.visit('/auth')
    
      cy.getBySel('logOut').click()
      cy.getBySel('nobodySignedIn').should('exist')
      cy.on('uncaught:exception', (err, runnable) => {
        return false
      })
    })

})
