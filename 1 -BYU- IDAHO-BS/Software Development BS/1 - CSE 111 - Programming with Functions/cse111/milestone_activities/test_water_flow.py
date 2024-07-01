#Last test function didn't pass and could not resolve at time
from pytest import approx
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
import pytest
import math

def test_water_column_height():
    arrayTest = [(0.0, 0.0, 0.0), (0.0, 10.0, 7.5),
                 (25.0, 0.0, 25.0), (48.3, 12.8, 57.9)]
    for line in arrayTest:
        tower_height, tankWall_height, water_column_height_result = line
        assert water_column_height(tower_height, tankWall_height) == water_column_height_result 


def test_pressure_gain_from_water_height():
     arrayTest = [(0.0, 0.000, 0.001), (30.2, 295.628, 0.001),
                 (50.0, 489.450, 0.001)]
     for line in arrayTest:
         height, expect_pressure, abs_tolerance = line
         result = pressure_gain_from_water_height(height)
         assert approx(result, abs_tolerance)  == expect_pressure

def test_pressure_loss_from_pipe():
      arrayTest = [ (0.048692, 0.00, 0.018, 1.75, 0.000, 0.001), (0.048692, 200.00, 0.000, 1.75, 0.000, 0.001), (0.048692, 200.00, 0.018, 0.00, 0.000, 0.001), (0.048692, 200.00, 0.018, 1.75, -113.008, 0.001), (0.048692, 200.00, 0.018, 1.65, -100.462, 0.001), (0.286870, 1000.00, 0.013, 1.65, -61.576, 0.001), (0.286870, 1800.75, 0.013, 1.65, -110.884, 0.001) ]
     
      for line in arrayTest:
           pipe_diameter, pipe_lengh, friction_factor, fluid_velocity, pressure_loss, abs_tolerance = line
           result = pressure_loss_from_pipe(pipe_diameter, pipe_lengh, friction_factor, fluid_velocity)
           assert approx(result, abs_tolerance) == pressure_loss

def test_pressure_loss_from_fittings():
     # Test data
        test_cases = [
            (0.00, 3, 0.000, 0.001),
            (1.65, 0, 0.000, 0.001),
            (1.65, 2, -0.109, 0.001),
            (1.75, 2, -0.122, 0.001),
            (1.75, 5, -0.306, 0.001),
        ]

        for fluid_velocity, quantity_of_fittings, expected_pressure_loss, absolute_tolerance in test_cases:
            pressure_loss = pressure_loss_from_fittings(fluid_velocity, quantity_of_fittings)
            assert math.isclose(pressure_loss, expected_pressure_loss, abs_tol=absolute_tolerance)
          
def test_reynolds_number():
        # Test data
        test_cases = [
            (0.048692, 0.00, 0, 1),
            (0.048692, 1.65, 80069, 1),
            (0.048692, 1.75, 84922, 1),
            (0.286870, 1.65, 471729, 1),
            (0.286870, 1.75, 500318, 1),
        ]

        for hydraulic_diameter, fluid_velocity, expected_reynolds_number, absolute_tolerance in test_cases:
            result = reynolds_number(hydraulic_diameter, fluid_velocity)
            assert approx(expected_reynolds_number, abs=absolute_tolerance) == result

def test_pressure_loss_from_pipe_reduction():
        # Test data
        # Test case 1
        larger_diameter = 0.28687
        fluid_velocity = 0.00
        reynolds_number = 1
        smaller_diameter = 0.048692
        expected_pressure_loss = 0.000
        approx_absolute_tolerance = 0.001

        result = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
        assert math.isclose(result, expected_pressure_loss, abs_tol=approx_absolute_tolerance), f"Test case 1 failed: expected {expected_pressure_loss}, got {result}"

        # Test case 2
        larger_diameter = 0.28687
        fluid_velocity = 1.65
        reynolds_number = 471729
        smaller_diameter = 0.048692
        expected_pressure_loss = -163.744
        approx_absolute_tolerance = 0.001

        result = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
        assert approx(expected_pressure_loss, approx_absolute_tolerance) == result, f"Test case 2 failed: expected {expected_pressure_loss}, got {result}"

        # Test case 3
        larger_diameter = 0.28687
        fluid_velocity = 1.75
        reynolds_number = 500318
        smaller_diameter = 0.048692
        expected_pressure_loss = -184.182
        approx_absolute_tolerance = 0.001

        result = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
        assert math.isclose(result, expected_pressure_loss, abs_tol=approx_absolute_tolerance), f"Test case 3 failed: expected {expected_pressure_loss}, got {result}"

        print("All test cases passed!")

pytest.main(["-v", "--tb=line", "-rN", __file__])
