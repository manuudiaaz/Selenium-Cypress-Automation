describe('My First Test', function() {
  it('Visits a website and checks the title', function() {
    cy.visit('https://example.com')
    cy.title().should('include', 'Example Domain')
  })
})
