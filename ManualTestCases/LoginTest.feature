Feature: I want to log-in into the site with valid and invalid credentials

  Background:
    Given I navigate to the Website

  Scenario: Log-in as standard user with valid data
    When I log-in as a standard user
    Then I should see the Products subtitle on the page

  Scenario: Login as a user with invalid username
    When I log-in with invalid username for a standard user
    Then I should see an error message
      | errormessage                                                              |
      | Epic sadface: Username and password do not match any user in this service |

  Scenario: Login as a user with invalid password
    When I log-in with invalid password for a standard user
    Then I should see an error message
      | errormessage                                                              |
      | Epic sadface: Username and password do not match any user in this service |

  Scenario: Login as a locked out user
    When I log-in as a locked out user
    Then I should see an error message
      | errormessage                                        |
      | Epic sadface: Sorry, this user has been locked out. |

  Scenario: Log-out
    Given I log-in as a standard user
    When I click Logout
    Then I should see Login page
