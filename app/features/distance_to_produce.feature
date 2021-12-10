Feature: Determine distance to produce from customer location
  Calculate distance to produce from a customer location

  Scenario: When a customer location is provided, show distance to produce
    Given POS TestPOS exists at location 40.6693521, -73.9336304
    And Produce Carrots are available at TestPOS
    Then User at location -71.0169325, 42.4068238 should see distance of produce Carrots at this POS is 9421.661593810348 miles
