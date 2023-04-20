/// <reference types="cypress" />


describe('Azure Active Directory Authentication', () => {
    before(() => {
      cy.loginToAAD(Cypress.env('aad_username'), Cypress.env('aad_password'))
    })
  

})
