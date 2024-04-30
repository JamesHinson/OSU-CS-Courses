// HW 4 Starter Code
// Name: James Hinson
// Date: 4/29/2024
// Description: All code must be commented. Add a description.

// student array creation
const students = [];

// Function Definition - Calculate Average Score
function calculateAverageScore(student) {
    var sum = student.studentScores.reduce((acc, score) => acc + score, 0);
    var avg = sum / student.studentScores.length;
    student.averageScore = avg;
}

// Function Definition - Assign Grade
function assignGrade(student) {
    if (student.averageScore >= 90) {
        student.grade = 'A';
    } else if (student.averageScore >= 80) {
        student.grade = 'B';
    } else if (student.averageScore >= 70) {
        student.grade = 'C';
    } else if (student.averageScore >= 60) {
        student.grade = 'D';
    } else {
        student.grade = 'F';
    }
}

// Function Definition - Display Student Information
function displayStudentInfo(student) {
    console.log(`Name: ${student.studentName}`);
    console.log(`Scores: ${student.studentScores.join(', ')}`);
    console.log(`Average Score: ${student.averageScore}`);
    console.log(`Grade: ${student.grade}`);
    console.log("---------------------------------------");
}

// Function Definition - Return the names of students with an average
// score >= 93
function findHighestGrades(students) {
    return students.filter(student => student.averageScore >= 93).map(student => student.studentName);
}

// Function Definition - Add Student to the Students Array
function addStudent(students, newStudent) {
    newStudent.averageScore = calculateAverageScore(newStudent);
    newStudent.grade = assignGrade(newStudent);
    students.push(newStudent);
}

// Student Object
function Student(name, scores) {
    this.studentName = name;
    this.studentScores = scores;
    this.averageScore = 0;
    this.grade = "";
}

const student1 = new Student("John Doe", [77, 92, 78, 90] );
const student2 = new Student("Sam Smith", [95, 96, 98, 88] );
const student3 = new Student("Amy Lee", [95, 92, 98, 93] );
const student4 = new Student("Ann Green", [75, 92, 78, 63] );
const student5 = new Student("Pat Jones", [75, 92, 78, 50,70] );

// Add students to the array
addStudent(students, student1);
addStudent(students, student2);
addStudent(students, student3);
addStudent(students, student4);
addStudent(students, student5);


// Prompt user to enter name of student and return the
// students information if the student is in the list otherwise
// indicate that the student was not found.
function findStudent(studentName) {
    const foundStudent = students.find(student => student.studentName === studentName);
    if (foundStudent) {
        displayStudentInfo(foundStudent);
    } else {
        console.log(`Student '${studentName}' not found.`);
    }
}

// Display student information
console.log("Display all Students:");
console.log("---------------------------------------");
students.forEach(student => displayStudentInfo(student));

// Find & display names of students with the average grades over 93
const highestGradesStudents = findHighestGrades(students);

// TO-DO finish

findStudent();
findStudent();
