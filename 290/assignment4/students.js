// HW 4 - Student Management System
// Name: James Hinson
// Date: 4/29/2024
// Description: This JavaScript program manages student data, including calculating average scores,
//              assigning grades, and displaying student information. It allows users to add new
//              students and find specific students by name.

// Student array creation
const students = [];

/****************************************************
** Name: calculateAverageScore
** Description: Calculates the average score for a student.
** Parameters: {object} student - The student object containing all student information
****************************************************/
function calculateAverageScore(student) {
  // Calculate sum of scores
  const sum = student.scores.reduce((total, score) => total + score, 0);
  // Calculate average score
  const average = sum / student.scores.length;
  // Update student's averageScore property
  student.averageScore = average;
}


/****************************************************
** Name: assignGrade
** Description: Assigns a grade to a student based on their average score.
** Parameters: {object} student - The student object containing all student information
****************************************************/
function assignGrade(student) {
  // Check average score and assign grade accordingly
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


/****************************************************
** Name: displayStudentInfo
** Description: Displays student information in a formatted style
** Parameters: {object} student - The student object containing all student information.
****************************************************/
function displayStudentInfo(student) {
  // Display student information
  console.log(`Name: ${student.name}`);
  console.log(`Scores: ${student.scores.join(', ')}`);
  console.log(`Average Score: ${student.averageScore}`);
  console.log(`Grade: ${student.grade}`);
  console.log("---------------------------------------");
}


/****************************************************
** Name: findHighestGrades
** Description: Finds all students with a high average grade (grades >= 93)
** Parameters: {object} student - The student object containing all student information
**             {object} students - The array containing student objects.
****************************************************/
function findHighestGrades(students) {
  // Filter students with average score >= 93 and return their names
  return students.filter(student => student.averageScore >= 93).map(student => student.name);
}


/****************************************************
** Name: addStudent
** Description: Adds a new student to the students array
** Parameters: {object} students - The array containing student objects.
**             {object} newStudent - The student object containing basic parameters.
****************************************************/
function addStudent(students, newStudent) {
  // Add new student to the students array
  students.push(newStudent);
}


/****************************************************
** Name: Student
** Description: Initializes a student object with default values.
** Parameters: name - The student's name to be submitted.
**             scores - The student's scores to be submitted.
****************************************************/
function Student(name, scores) {
  // Initialize student object properties
  this.name = name;
  this.scores = scores;
  this.averageScore = 0; // Initialize average score
  this.grade = ""; // Initialize grade
}

// Create student objects
const student1 = new Student("John Doe", [77, 92, 78, 90]);
const student2 = new Student("Sam Smith", [95, 96, 98, 88]);
const student3 = new Student("Amy Lee", [95, 92, 98, 93]);
const student4 = new Student("Ann Green", [75, 92, 78, 63]);
const student5 = new Student("Pat Jones", [75, 92, 78, 50, 70]);

// Add students to the array
addStudent(students, student1);
addStudent(students, student2);
addStudent(students, student3);
addStudent(students, student4);
addStudent(students, student5);

// Calculate and assign average score and grade to each student
students.forEach(student => calculateAverageScore(student));
students.forEach(student => assignGrade(student));


/*******************************************
** Name: findStudent
** Description: Prompts the user for a student's name and displays the student's information if found.
** Parameters: {object} student - The student object containing all student information
*******************************************/
function findStudent() {
  // Prompt user for student's name
  const name = prompt("Enter a student's full name:");
  // Find student in the students array
  const foundStudent = students.find(student => student.name === name);
  if (foundStudent) {
    // If student found, display student information
    displayStudentInfo(foundStudent);
  } else {
    // If student not found, display message
    console.log(`Student '${name}' not found.`);
  }
}

// Display student information
console.log("Display all Students:");
console.log("---------------------------------------");
students.forEach(student => displayStudentInfo(student));

// Find & display names of students with the average grades over 93
const highestGradesStudents = findHighestGrades(students);
console.log("Students with average grades over 93:");
console.log(highestGradesStudents);

// Find unique students based on user input
findStudent();
findStudent();