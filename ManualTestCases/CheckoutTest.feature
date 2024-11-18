Feature: I want to see and manipulate products added to the Cart

  Background:
    Given I login as a standard user
    And I navigate to the Products page
    And I add one product to the Cart
    And I go to Cart
    And I click on Checkout button

  Scenario: Successfully redirected to Overview page
    Given I fill the form with valid first name, last name, postal code
    When I click Continue
    Then I should be redirected to Overview page
    And I should see that there is only one product on the list in Overview

  Scenario: Go to Overview without giving a first name
    Given I fill the form with a valid last name and postal code
    When I click Continue
    Then I should stay on the Your Information page
    And I should see an error message
      | errormessage                  |
      | Error: First Name is required |

  Scenario: Go to Overview without giving a last name
    Given I fill the form with a valid first name and postal code
    When I click Continue
    Then I should stay on the Your Information page
    And I should see an error message
      | errormessage                 |
      | Error: Last Name is required |

  Scenario: Go to Overview without giving a postal code
    Given I fill the form with a valid first name and last name
    When I click Continue
    Then I should stay on the Your Information page
    And I should see an error message
      | errormessage                   |
      | Error: Postal Code is required |

  Scenario: Go back from Your information to Cart
    Given I fill the form with valid first name, last name, zip code
    When I click Cancel
    Then I should be redirected to the Cart page
    And Cart is not empty

  Scenario: Successfully finish the order
    Given I fill the form with valid first name, last name, zip code
    And I click Continue
    When I click Finish
    Then I should be redirected to the Finish page
    And Cart is empty

  Scenario: Go back from Overview to Products
    Given I fill the form with valid first name, last name, zip code
    And I click Continue
    When I click Cancel
    Then I should be redirected to the Products page
    And Cart is not empty
