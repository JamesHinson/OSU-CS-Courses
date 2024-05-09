/*
Name: James Hinson
Course: CS290 - Web Development
Date: 5/8/2024
*/

// Global variables to track goal, wins, and losses
let goalNum = 0;
let winsNum = 0;
let lossesNum = 0;

// Global variables to track selected numbers and operator
let firstNum = 0;
let secondNum = 0;
let operator = "";

// Global array to store game status values and variable to store current game status
const gameStatus = {
    START: 1,
    PICK_FIRST_NUMBER: 2,
    PICK_OPERATOR: 3,
    PICK_SECOND_NUMBER: 4,
    WIN: 5,
    LOSE: 6
};
let gameStatusValue = gameStatus.START;

// Function to get all number grid buttons
function getNumberGridButtons() {
    return document.querySelectorAll("#numberGrid > button");
}

// Function to get all operator list buttons
function getOperatorButtons() {
    return document.querySelectorAll("#operatorList > button");
}

// Function to generate a new game
function newGame() {
    const numberButtons = getNumberGridButtons();
    for (let button of numberButtons) {
        button.removeAttribute("disabled");
        button.textContent = Math.floor(Math.random() * 10 + 1);
        button.removeAttribute("disabled");
    }

    let workSpace = document.getElementById("work");
    while (workSpace.hasChildNodes()) {
        workSpace.removeChild(workSpace.firstChild);
    }

    document.getElementById("goal").innerText = generateGoal();
    document.getElementById("gameStatus").innerText = "Let's Play!"
    gameStatusValue = gameStatus.START;
}

// Function to generate a goal number
function generateGoal() {
    let numbers = [];
    let numberButtons = getNumberGridButtons();
    for (let button of numberButtons) {
        numbers.push(parseInt(button.textContent))
    }

    let x = Math.floor(Math.random() * 4);
    let y = Math.floor(Math.random() * 4);
    let z = Math.floor(Math.random() * 4);
    while (x === y || x === z || z === y) {
        x = Math.floor(Math.random() * 4);
        y = Math.floor(Math.random() * 4);
        z = Math.floor(Math.random() * 4);
    }

    let operator = Math.floor(Math.random() * 3);
    let operator2 = Math.floor(Math.random() * 3);

    if (operator === 0) {
        if (operator2 === 0) {
            goalNum = (numbers[x] + numbers[y]) + numbers[z];
        } else if (operator2 === 1) {
            goalNum = (numbers[x] + numbers[y]) - numbers[z];
        } else {
            goalNum = (numbers[x] + numbers[y]) * numbers[z];
        }
    } else if (operator === 1) {
        if (operator2 === 0) {
            goalNum = (numbers[x] - numbers[y]) + numbers[z];
        } else if (operator2 === 1) {
            goalNum = (numbers[x] - numbers[y]) - numbers[z];
        } else {
            goalNum = (numbers[x] - numbers[y]) * numbers[z];
        }
    } else {
        if (operator2 === 0) {
            goalNum = (numbers[x] * numbers[y]) * numbers[z];
        } else if (operator2 === 1) {
            goalNum = (numbers[x] * numbers[y]) * numbers[z];
        } else {
            goalNum = (numbers[x] * numbers[y]) * numbers[z];
        }
    }
    return goalNum;
}

// Function called when a number button is clicked
function boardButtonClicked(button) {
    if (gameStatusValue === gameStatus.START || gameStatusValue === gameStatus.PICK_FIRST_NUMBER) {
        let num = button.textContent;
        firstNum = parseInt(num);

        button.disabled = true;

        gameStatusValue = gameStatus.PICK_OPERATOR;
        document.getElementById("gameStatus").innerText = "Select an operator";
    } else if (gameStatusValue === gameStatus.PICK_SECOND_NUMBER) {
        let num = button.textContent;
        secondNum = parseInt(num);

        button.disabled = true;
        button.textContent = "";

        let numberButtons = getNumberGridButtons();
        for (let button of numberButtons) {
            if (button.disabled === true) {
                button.textContent = "";
            }
        }
        checkResult();
    }
}

// Function called when an operator button is clicked
function operatorButtonClicked(button) {
    if (gameStatusValue === gameStatus.PICK_OPERATOR) {
        let operatorSign = button.textContent;
        operator = operatorSign;

        button.disabled = true;

        gameStatusValue = gameStatus.PICK_SECOND_NUMBER;
        document.getElementById("gameStatus").innerText = "Select a number";
    }
}

// Function to check the result after user input
function checkResult() {
    let result = 0;
    if (operator === "+") {
        result = firstNum + secondNum;
    } else if (operator === "-") {
        result = firstNum - secondNum;
    } else {
        result = firstNum * secondNum;
    }

    let numberButtons = getNumberGridButtons();
    for (let button of numberButtons) {
        if (button.disabled === true) {
            button.textContent = result;
            button.removeAttribute("disabled");
            break;
        }
    }

    let operatorButtons = getOperatorButtons();
    for (let button of operatorButtons) {
        if (button.disabled === true) {
            button.removeAttribute("disabled");
            break;
        }
    }

    let text = document.createTextNode(firstNum + " " + operator + " " + secondNum + " " + "= " + result)
    let br = document.createElement("br");
    document.getElementById("work").appendChild(text);
    document.getElementById("work").appendChild(br);

    if (result === goalNum) {
        document.getElementById("wins").textContent = ++winsNum;
        gameStatusValue = gameStatus.WIN;
        document.getElementById("gameStatus").innerText = "You won!!!"
    } else if (checkKeepPlaying()) {
        gameStatusValue = gameStatus.PICK_FIRST_NUMBER;
        document.getElementById("gameStatus").innerText = "Select a number";
    } else {
        document.getElementById("losses").textContent = ++lossesNum;
        gameStatusValue = gameStatus.LOSE;
        document.getElementById("gameStatus").innerText = "Game Over! Better Luck Next Time";
    }
}

// Function to check if there are sufficient options to keep playing
function checkKeepPlaying() {
    let numberButtons = getNumberGridButtons();
    let available = 4;
    for (let button of numberButtons) {
        if (button.disabled === true) {
            available--;
        }
    }
    
    return available >= 2;
}

// Event listener for when the DOM is loaded
document.addEventListener("DOMContentLoaded", function() {
    const newBtn = document.getElementById("newGame");
    newBtn.addEventListener("click", newGame);

    const numberButtons = getNumberGridButtons();
    for (let button of numberButtons) {
        button.addEventListener("click", () => boardButtonClicked(button));
    }

    const operatorButtons = getOperatorButtons();
    for (let button of operatorButtons) {
        button.addEventListener("click", () => operatorButtonClicked(button));
    }

    document.getElementById("wins").textContent = winsNum;
    document.getElementById("losses").textContent = lossesNum;

    newGame();
});
