const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber with type equal to SUM', function () {
  it('check that two numbers without float part are the expected sum', function () {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1, 8)).to.equal(9);
    expect(calculateNumber('SUM', 5, 7)).to.equal(12);
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it('check that the sum is working correctly with negative numbers', function () {
    expect(calculateNumber('SUM', -5, 10)).to.equal(5);
    expect(calculateNumber('SUM', -6, -12)).to.equal(-18);
    expect(calculateNumber('SUM', -999, -1)).to.equal(-1000);
    expect(calculateNumber('SUM', 5, -10)).to.equal(-5);
  });
  it('The sum is executed correctly with a 0', function () {
    expect(calculateNumber('SUM', 0, 5)).to.equal(5);
    expect(calculateNumber('SUM', 10, 0)).to.equal(10);
    expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    expect(calculateNumber('SUM', -30, 0)).to.equal(-30);
  });
  it('Check in sum first number is integer number and second number is float number', function () {
    expect(calculateNumber('SUM', 14, 0.7)).to.equal(15);
    expect(calculateNumber('SUM', 14, 0.4)).to.equal(14);
  });
  it('Check in sum second number is integer number and first number is float number', function () {
    expect(calculateNumber('SUM', 0.7, 14)).to.equal(15);
    expect(calculateNumber('SUM', 0.4, 14)).to.equal(14);
  });
});

describe('calculateNumber with type equal to SUBTRACT', function () {
  it('check that two numbers without float part are the expected subtract', function () {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', 1, 8)).to.equal(-7);
    expect(calculateNumber('SUBTRACT', 5, 7)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it('check that the subtract is working correctly with negative numbers', function () {
    expect(calculateNumber('SUBTRACT', -5, 10)).to.equal(-15);
    expect(calculateNumber('SUBTRACT', -6, -12)).to.equal(6);
    expect(calculateNumber('SUBTRACT', -999, -1)).to.equal(-998);
    expect(calculateNumber('SUBTRACT', 5, -10)).to.equal(15);
  });
  it('The subtract is executed correctly with a 0', function () {
    expect(calculateNumber('SUBTRACT', 0, 5)).to.equal(-5);
    expect(calculateNumber('SUBTRACT', 10, 0)).to.equal(10);
    expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    expect(calculateNumber('SUBTRACT', -30, 0)).to.equal(-30);
  });
  it('Check first number is integer number and second number is float number', function () {
    expect(calculateNumber('SUBTRACT', 14, 0.7)).to.equal(13);
    expect(calculateNumber('SUBTRACT', 14, 0.4)).to.equal(14);
  });
  it('Check in subtract second number is integer number and first number is float number', function () {
    expect(calculateNumber('SUBTRACT', 0.7, 14)).to.equal(-13);
    expect(calculateNumber('SUBTRACT', 0.4, 14)).to.equal(-14);
  });
});

describe('calculateNumber with type equal to DIVIDE', function () {
  it('log an error when second number is 0', function () {
    expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', -5, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', -50.8, 0)).to.equal('Error');
  });
  it('log the expected result when second number is not 0', function () {
    expect(calculateNumber('DIVIDE', 1, 3)).to.equal(0.33);
    expect(calculateNumber('DIVIDE', 1, 8)).to.equal(0.13);
    expect(calculateNumber('DIVIDE', 5, 7)).to.equal(0.71);
    expect(calculateNumber('DIVIDE', 5, 5)).to.equal(1);
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
});

describe('calculateNumber with an incorrect type', function () {
  it('Expect to be undefined if type is not SUM, SUBTRACT or DIVIDE', function () {
    expect(calculateNumber('DIV', 1, 3)).to.equal(undefined);
    expect(calculateNumber('DIV', 1, 8)).to.equal(undefined);
    expect(calculateNumber('DIV', 5, 7)).to.equal(undefined);
  });
});
