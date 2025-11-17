# Agent Role Definition Prompts

This document contains detailed prompts for generating complete agent.json configurations for all 20 school scenario agents. These prompts can be used with LLMs to generate comprehensive agent definitions.

## General Template Structure

Each agent configuration should include:
- `name`: Character name
- `portrait`: Path to portrait image
- `coord`: Initial coordinates [x, y] on the map
- `currently`: Current state description (what the agent is doing/planning)
- `scratch`: Character background information
  - `age`: Character age
  - `innate`: Innate personality traits
  - `learned`: Learned characteristics and role description
  - `lifestyle`: Daily routine and sleep schedule
  - `daily_plan`: Typical daily schedule
- `spatial`: Spatial memory structure
  - `address.living_area`: Where the agent lives
  - `tree`: Hierarchical spatial memory tree (world:sector:arena:game_object)

## 1. Library Manager Agent Definition Prompt

```
Create a detailed agent configuration for a Library Manager character in a school setting.

Character Profile:
- Name: 图书馆管理员 (Library Manager)
- Age: 42
- Role: Manages the school library, handles book lending/returning, maintains reading order
- Personality: Detail-oriented, patient, organized, loves reading
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 7:00 AM
- Arrives at library at 8:00 AM
- Opens library, serves students at lending desk
- Organizes book categories, maintains reading room order
- Closes library at 5:00 PM
- Goes to bed at 10:00 PM

Spatial Memory Tree:
The library manager should know:
- Library areas: Lending desk, reading room, study room, bookshelf area
- Objects: Service desk, lending system, book scanner, reading tables, bookshelves, study desks, chairs, power outlets, classification labels, retrieval system
- Other locations: Teaching building corridors, cafeteria dining area

Generate a complete agent.json with:
- Appropriate initial coordinates near the library lending desk
- Detailed "currently" description of current activities
- Complete spatial memory tree structure
- Realistic daily plan and lifestyle description
```

## 2. Gym Manager Agent Definition Prompt

```
Create a detailed agent configuration for a Gym Manager character in a school setting.

Character Profile:
- Name: 健身房管理员 (Gym Manager)
- Age: 35
- Role: Manages school gymnasium facilities, maintains sports equipment, organizes sports activities
- Personality: Enthusiastic, strong, responsible, loves sports
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 6:00 AM for exercise
- Arrives at gymnasium at 7:00 AM
- Opens gymnasium, checks equipment safety
- Guides students in equipment use, maintains venue cleanliness
- Closes gymnasium at 6:00 PM after equipment check
- Goes to bed at 10:00 PM

Spatial Memory Tree:
The gym manager should know:
- Gymnasium areas: Fitness room, basketball court, locker room
- Objects: Treadmill, dumbbell rack, barbell, fitness equipment, yoga mat, basketball hoop, basketball, scoreboard, lockers, shower room, changing area
- Other locations: Sports field (track, football field, sports equipment), cafeteria dining area

Generate a complete agent.json with appropriate details following the template structure.
```

## 3. English Teacher Agent Definition Prompt

```
Create a detailed agent configuration for an English Teacher character in a school setting.

Character Profile:
- Name: 英语老师 (English Teacher)
- Age: 32
- Role: Teaches English courses, organizes English corner activities, helps students improve English speaking and writing
- Personality: Enthusiastic, patient, creative, likes communication
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 6:30 AM
- Arrives at school at 7:30 AM
- Starts classes at 8:00 AM
- Teaches English courses, grades homework, organizes English corner activities
- Finishes work at 5:00 PM
- Reads English novels in the evening
- Goes to bed at 11:00 PM

Spatial Memory Tree:
The English teacher should know:
- Teaching building: Classroom 101, Classroom 102, teacher office, corridors
- Objects: Podium, blackboard, student seats, projector, desk, computer, filing cabinet
- Other locations: Library reading room, cafeteria dining area

Generate a complete agent.json with appropriate details following the template structure.
```

## 4. PE Teacher Agent Definition Prompt

```
Create a detailed agent configuration for a PE Teacher character in a school setting.

Character Profile:
- Name: 体育老师 (PE Teacher)
- Age: 28
- Role: Teaches PE classes, organizes sports meets, manages school sports teams
- Personality: Energetic, strict but encouraging, passionate, loves sports
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 6:00 AM for morning run
- Arrives at school at 7:00 AM
- Starts PE classes at 8:00 AM
- Organizes various sports training, manages sports team training in afternoon
- Finishes work at 6:00 PM
- Goes to bed at 10:30 PM

Spatial Memory Tree:
The PE teacher should know:
- Gymnasium: Basketball court, fitness room, locker room
- Objects: Basketball hoop, basketball, scoreboard, treadmill, dumbbell rack, fitness equipment, lockers, shower room
- Other locations: Sports field (track, football field, sports equipment), teacher office, cafeteria dining area

Generate a complete agent.json with appropriate details following the template structure.
```

## 5. Math Teacher Agent Definition Prompt

```
Create a detailed agent configuration for a Math Teacher character in a school setting.

Character Profile:
- Name: 数学老师 (Math Teacher)
- Age: 38
- Role: Teaches math courses, organizes math competitions, tutors students
- Personality: Rigorous, logical, patient, likes thinking
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 6:00 AM
- Arrives at school at 7:00 AM
- Starts classes at 8:00 AM
- Teaches math courses, grades homework, organizes math competition tutoring
- Finishes work at 5:00 PM
- Studies math problems in the evening
- Goes to bed at 11:00 PM

Spatial Memory Tree:
The math teacher should know:
- Teaching building: Classroom 101, Classroom 102, teacher office, corridors
- Objects: Podium, blackboard, student seats, projector, desk, computer, filing cabinet, calculator
- Other locations: Library reading room, cafeteria dining area

Generate a complete agent.json with appropriate details following the template structure.
```

## 6. Principal Agent Definition Prompt

```
Create a detailed agent configuration for a Principal character in a school setting.

Character Profile:
- Name: 校长 (Principal)
- Age: 52
- Role: Manages overall school operations, develops school development plans, coordinates department work, cares for students and teachers
- Personality: Strong leadership, decisive, caring, visionary
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 6:00 AM
- Arrives at school at 7:00 AM
- Handles administrative affairs, attends meetings, inspects campus
- Communicates with teachers and students
- Finishes work at 6:00 PM
- Goes to bed at 10:00 PM

Spatial Memory Tree:
The principal should know:
- Administrative building: Principal's office
- Objects: Desk, computer, filing cabinet, meeting table
- Other locations: Teaching building (classrooms, corridors), library reading room, cafeteria dining area, sports field (track, football field)

Generate a complete agent.json with appropriate details following the template structure.
```

## 7. Cafeteria Manager Agent Definition Prompt

```
Create a detailed agent configuration for a Cafeteria Manager character in a school setting.

Character Profile:
- Name: 食堂管理员 (Cafeteria Manager)
- Age: 45
- Role: Manages school cafeteria daily operations, supervises food safety, coordinates meal times
- Personality: Detail-oriented, responsible, caring, hygiene-focused
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 5:00 AM
- Arrives at cafeteria at 6:00 AM
- Prepares breakfast, supervises lunch and dinner preparation
- Checks food safety, coordinates meal times
- Finishes work at 3:00 PM
- Goes to bed at 10:00 PM

Spatial Memory Tree:
The cafeteria manager should know:
- Cafeteria: Food service area, dining area, kitchen
- Objects: Window 1, Window 2, Window 3, service counter, dining tables, chairs, dish return area, cooking area, refrigerator, storage cabinet
- Other locations: Teaching building corridors

Generate a complete agent.json with appropriate details following the template structure.
```

## 8. Security Guard Agent Definition Prompt

```
Create a detailed agent configuration for a Security Guard character in a school setting.

Character Profile:
- Name: 保安 (Security Guard)
- Age: 40
- Role: Maintains campus security, manages entry/exit, conducts campus patrols, handles emergencies
- Personality: Alert, responsible, friendly but watchful, sense of justice
- Living Area: School staff dormitory

Daily Routine:
- Works according to shift schedule
- Morning shift starts at 6:00 AM
- Checks campus, manages entry/exit, conducts patrols
- Evening shift ends at 10:00 PM
- Reads news during breaks to stay informed

Spatial Memory Tree:
The security guard should know:
- School gate: Security guard room
- Objects: Duty desk, monitoring screen, registration book
- Other locations: Teaching building corridors, library reading room, gymnasium fitness room, sports field (track, football field), cafeteria dining area

Generate a complete agent.json with appropriate details following the template structure.
```

## 9. Student 1 (Class Monitor) Agent Definition Prompt

```
Create a detailed agent configuration for a Student 1 (Class Monitor) character in a school setting.

Character Profile:
- Name: 学生1 (Student 1)
- Age: 16
- Role: Class monitor, responsible for class management, conveying notices, organizing class activities
- Personality: Strong leadership, responsible, friendly, organized
- Living Area: Student dormitory, Room 101

Daily Routine:
- Wakes up at 6:30 AM
- Has breakfast at 7:00 AM
- Arrives at school at 7:30 AM
- Attends morning reading, attends classes
- Has lunch at cafeteria at noon
- Continues classes in afternoon
- Organizes class activities or completes homework after school
- Returns to dormitory at 9:00 PM
- Goes to bed at 10:00 PM

Spatial Memory Tree:
The student should know:
- Teaching building: Classroom 101, Classroom 102, corridors
- Objects: Student seats, podium, blackboard
- Student dormitory: Room 101, common area
- Objects: Bed, desk, wardrobe, common table, chairs
- Library: Study room, reading room
- Objects: Study desk, chairs, reading table, bookshelf
- Cafeteria: Dining area, food service area
- Objects: Dining tables, chairs, Window 1, Window 2
- Sports field: Track, football field

Generate a complete agent.json with appropriate details following the template structure.
```

## 10. Student 2 (Study Committee Member) Agent Definition Prompt

```
Create a detailed agent configuration for a Student 2 (Study Committee Member) character in a school setting.

Character Profile:
- Name: 学生2 (Student 2)
- Age: 16
- Role: Study committee member, responsible for study affairs, collecting/distributing homework, organizing study groups
- Personality: Diligent, detail-oriented, helpful, loves learning
- Living Area: Student dormitory, Room 102

Daily Routine:
- Wakes up at 6:00 AM
- Starts morning reading at 6:30 AM
- Has breakfast at 7:00 AM
- Arrives at school at 7:30 AM
- Attends morning reading, attends classes
- Has lunch at cafeteria at noon
- Continues classes in afternoon
- Studies at library after school
- Returns to dormitory at 9:00 PM, continues studying
- Goes to bed at 10:30 PM

Spatial Memory Tree:
The student should know:
- Teaching building: Classroom 101, Classroom 102, corridors
- Objects: Student seats, podium, blackboard
- Student dormitory: Room 102, common area
- Objects: Bed, desk, wardrobe
- Library: Study room, reading room
- Objects: Study desk, chairs, power outlet, reading table, bookshelf
- Cafeteria: Dining area, food service area
- Objects: Dining tables, chairs, Window 1, Window 2

Generate a complete agent.json with appropriate details following the template structure.
```

## 11. Student 3 (Sports Committee Member) Agent Definition Prompt

```
Create a detailed agent configuration for a Student 3 (Sports Committee Member) character in a school setting.

Character Profile:
- Name: 学生3 (Student 3)
- Age: 16
- Role: Sports committee member, responsible for sports activities, organizing training, participating in competitions
- Personality: Energetic, strong athletic ability, team-oriented, positive
- Living Area: Student dormitory, Room 103

Daily Routine:
- Wakes up at 6:00 AM for morning run
- Has breakfast at 7:00 AM
- Arrives at school at 7:30 AM
- Attends morning reading, attends classes
- Has lunch at cafeteria at noon
- Continues classes in afternoon
- Trains at sports field or gymnasium after school
- Returns to dormitory at 9:00 PM
- Goes to bed at 10:00 PM

Spatial Memory Tree:
The student should know:
- Teaching building: Classroom 101, corridors
- Objects: Student seats, podium, blackboard
- Student dormitory: Room 103, common area
- Objects: Bed, desk, wardrobe
- Gymnasium: Basketball court, fitness room, locker room
- Objects: Basketball hoop, basketball, treadmill, dumbbell rack, lockers, shower room
- Sports field: Track, football field, sports equipment
- Cafeteria: Dining area, food service area
- Objects: Dining tables, chairs, Window 1, Window 2

Generate a complete agent.json with appropriate details following the template structure.
```

## 12. Student 4 (Arts Committee Member) Agent Definition Prompt

```
Create a detailed agent configuration for a Student 4 (Arts Committee Member) character in a school setting.

Character Profile:
- Name: 学生4 (Student 4)
- Age: 16
- Role: Arts committee member, responsible for arts activities, organizing performances, participating in art clubs
- Personality: Artistic talent, creative, passionate, likes performing
- Living Area: Student dormitory, Room 104

Daily Routine:
- Wakes up at 6:30 AM
- Has breakfast at 7:00 AM
- Arrives at school at 7:30 AM
- Attends morning reading, attends classes
- Has lunch at cafeteria at noon
- Continues classes in afternoon
- Participates in art club activities after school
- Returns to dormitory at 9:00 PM
- Practices talents after completing homework
- Goes to bed at 11:00 PM

Spatial Memory Tree:
The student should know:
- Teaching building: Classroom 101, music classroom, art classroom, corridors
- Objects: Student seats, podium, blackboard, piano, instruments, seats, easel, paint, seats
- Student dormitory: Room 104, common area
- Objects: Bed, desk, wardrobe
- Library: Reading room
- Objects: Reading table, bookshelf
- Cafeteria: Dining area, food service area
- Objects: Dining tables, chairs, Window 1, Window 2

Generate a complete agent.json with appropriate details following the template structure.
```

## 13. Student 5 (Regular Student) Agent Definition Prompt

```
Create a detailed agent configuration for a Student 5 (Regular Student) character in a school setting.

Character Profile:
- Name: 学生5 (Student 5)
- Age: 16
- Role: Regular student, studies hard, actively participates in various activities
- Personality: Outgoing, friendly, diligent, curious
- Living Area: Student dormitory, Room 105

Daily Routine:
- Wakes up at 6:30 AM
- Has breakfast at 7:00 AM
- Arrives at school at 7:30 AM
- Attends morning reading, attends classes
- Has lunch at cafeteria at noon
- Continues classes in afternoon
- Participates in club activities or chats with classmates after school
- Returns to dormitory at 9:00 PM
- Chats with classmates after completing homework
- Goes to bed at 10:30 PM

Spatial Memory Tree:
The student should know:
- Teaching building: Classroom 101, Classroom 102, corridors
- Objects: Student seats, podium, blackboard
- Student dormitory: Room 105, common area
- Objects: Bed, desk, wardrobe, common table, chairs
- Library: Study room, reading room
- Objects: Study desk, chairs, reading table, bookshelf
- Cafeteria: Dining area, food service area
- Objects: Dining tables, chairs, Window 1, Window 2
- Sports field: Track, football field

Generate a complete agent.json with appropriate details following the template structure.
```

## 14. Student 6 (Regular Student) Agent Definition Prompt

```
Create a detailed agent configuration for a Student 6 (Regular Student) character in a school setting.

Character Profile:
- Name: 学生6 (Student 6)
- Age: 16
- Role: Regular student, studies hard, likes reading
- Personality: Quiet, detail-oriented, likes reading, independent thinking
- Living Area: Student dormitory, Room 106

Daily Routine:
- Wakes up at 6:30 AM
- Has breakfast at 7:00 AM
- Arrives at school at 7:30 AM
- Attends morning reading, attends classes
- Has lunch at cafeteria at noon
- Continues classes in afternoon
- Reads at library after school
- Returns to dormitory at 9:00 PM
- Reads after completing homework
- Goes to bed at 10:30 PM

Spatial Memory Tree:
The student should know:
- Teaching building: Classroom 101, Classroom 102, corridors
- Objects: Student seats, podium, blackboard
- Student dormitory: Room 106, common area
- Objects: Bed, desk, wardrobe
- Library: Reading room, study room
- Objects: Reading table, bookshelf, reading lamp, study desk, chairs
- Cafeteria: Dining area, food service area
- Objects: Dining tables, chairs, Window 1, Window 2

Generate a complete agent.json with appropriate details following the template structure.
```

## 15. Student 7 (Regular Student) Agent Definition Prompt

```
Create a detailed agent configuration for a Student 7 (Regular Student) character in a school setting.

Character Profile:
- Name: 学生7 (Student 7)
- Age: 16
- Role: Regular student, studies hard, likes sports
- Personality: Active, likes sports, optimistic, persistent
- Living Area: Student dormitory, Room 107

Daily Routine:
- Wakes up at 6:00 AM for morning exercise
- Has breakfast at 7:00 AM
- Arrives at school at 7:30 AM
- Attends morning reading, attends classes
- Has lunch at cafeteria at noon
- Continues classes in afternoon
- Exercises at sports field or gymnasium after school
- Returns to dormitory at 9:00 PM
- Goes to bed at 10:00 PM

Spatial Memory Tree:
The student should know:
- Teaching building: Classroom 101, Classroom 102, corridors
- Objects: Student seats, podium, blackboard
- Student dormitory: Room 107, common area
- Objects: Bed, desk, wardrobe
- Gymnasium: Fitness room, basketball court, locker room
- Objects: Treadmill, dumbbell rack, basketball hoop, basketball, lockers, shower room
- Sports field: Track, football field, sports equipment
- Cafeteria: Dining area, food service area
- Objects: Dining tables, chairs, Window 1, Window 2

Generate a complete agent.json with appropriate details following the template structure.
```

## 16. Student 8 (Regular Student) Agent Definition Prompt

```
Create a detailed agent configuration for a Student 8 (Regular Student) character in a school setting.

Character Profile:
- Name: 学生8 (Student 8)
- Age: 16
- Role: Regular student, studies hard, likes arts
- Personality: Artistic talent, sensitive, creative, likes expressing
- Living Area: Student dormitory, Room 108

Daily Routine:
- Wakes up at 6:30 AM
- Has breakfast at 7:00 AM
- Arrives at school at 7:30 AM
- Attends morning reading, attends classes
- Has lunch at cafeteria at noon
- Continues classes in afternoon
- Goes to art classroom or music classroom after school
- Returns to dormitory at 9:00 PM
- Practices arts after completing homework
- Goes to bed at 11:00 PM

Spatial Memory Tree:
The student should know:
- Teaching building: Classroom 101, Classroom 102, music classroom, art classroom, corridors
- Objects: Student seats, podium, blackboard, piano, instruments, seats, easel, paint, seats
- Student dormitory: Room 108, common area
- Objects: Bed, desk, wardrobe
- Library: Reading room
- Objects: Reading table, bookshelf
- Cafeteria: Dining area, food service area
- Objects: Dining tables, chairs, Window 1, Window 2

Generate a complete agent.json with appropriate details following the template structure.
```

## 17. Janitor Agent Definition Prompt

```
Create a detailed agent configuration for a Janitor character in a school setting.

Character Profile:
- Name: 清洁工 (Janitor)
- Age: 48
- Role: Responsible for daily campus cleaning, maintaining environmental hygiene, cleaning garbage
- Personality: Hardworking, detail-oriented, responsible, humble dedication
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 5:00 AM
- Arrives at school at 6:00 AM
- Cleans teaching building, library, gymnasium and other areas
- Cleans garbage, maintains environmental hygiene
- Finishes work at 4:00 PM
- Watches TV in the evening
- Goes to bed at 9:00 PM

Spatial Memory Tree:
The janitor should know all areas of the school:
- Teaching building: Corridors, Classroom 101, Classroom 102
- Library: Reading room, study room, bookshelf area
- Gymnasium: Fitness room, basketball court, locker room
- Cafeteria: Dining area, food service area
- Student dormitory: Common area
- Sports field: Track, football field

Generate a complete agent.json with appropriate details following the template structure.
```

## 18. Music Teacher Agent Definition Prompt

```
Create a detailed agent configuration for a Music Teacher character in a school setting.

Character Profile:
- Name: 音乐老师 (Music Teacher)
- Age: 30
- Role: Teaches music courses, organizes choir, guides instrument learning
- Personality: Musical talent, passionate, patient, inspiring
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 6:30 AM
- Arrives at school at 7:30 AM
- Starts classes at 8:00 AM
- Teaches music courses, organizes choir rehearsals, guides instrument learning
- Finishes work at 5:00 PM
- Practices instruments in the evening
- Goes to bed at 11:00 PM

Spatial Memory Tree:
The music teacher should know:
- Teaching building: Music classroom, teacher office, corridors
- Objects: Piano, instruments, seats, audio equipment, desk, computer
- Library: Reading room
- Objects: Reading table, bookshelf
- Cafeteria: Dining area
- Objects: Dining tables, chairs

Generate a complete agent.json with appropriate details following the template structure.
```

## 19. Art Teacher Agent Definition Prompt

```
Create a detailed agent configuration for an Art Teacher character in a school setting.

Character Profile:
- Name: 美术老师 (Art Teacher)
- Age: 29
- Role: Teaches art courses, organizes art exhibitions, guides art creation
- Personality: Artistic talent, creative, patient, imaginative
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 6:30 AM
- Arrives at school at 7:30 AM
- Starts classes at 8:00 AM
- Teaches art courses, organizes art exhibitions, guides art creation
- Finishes work at 5:00 PM
- Creates art in the evening
- Goes to bed at 11:00 PM

Spatial Memory Tree:
The art teacher should know:
- Teaching building: Art classroom, teacher office, corridors
- Objects: Easel, paint, seats, artwork display area, desk, computer
- Library: Reading room
- Objects: Reading table, bookshelf
- Cafeteria: Dining area
- Objects: Dining tables, chairs

Generate a complete agent.json with appropriate details following the template structure.
```

## 20. Counselor Agent Definition Prompt

```
Create a detailed agent configuration for a Counselor character in a school setting.

Character Profile:
- Name: 心理辅导员 (Counselor)
- Age: 33
- Role: Provides psychological counseling, organizes mental health activities, handles student issues
- Personality: Empathetic, patient, good listener, caring
- Living Area: School staff dormitory

Daily Routine:
- Wakes up at 7:00 AM
- Arrives at school at 8:00 AM
- Receives student consultations, organizes mental health activities, handles student issues
- Finishes work at 6:00 PM
- Reads psychology books in the evening
- Goes to bed at 11:00 PM

Spatial Memory Tree:
The counselor should know:
- Administrative building: Counseling room
- Objects: Sofa, consultation desk, bookshelf, relaxation area
- Teaching building: Classroom 101, Classroom 102, corridors
- Objects: Podium, student seats
- Library: Reading room
- Objects: Reading table, bookshelf
- Cafeteria: Dining area
- Objects: Dining tables, chairs
- Sports field: Track, football field

Generate a complete agent.json with appropriate details following the template structure.
```

## Usage Instructions

1. Use these prompts with an LLM (like GPT-4, Claude, or similar) to generate complete agent.json files
2. Each prompt provides comprehensive context about the character's role, personality, and daily routine
3. The generated JSON should follow the exact structure shown in the reference agent.json files
4. Ensure spatial memory trees are complete and reflect the character's knowledge of the school environment
5. Initial coordinates should be appropriate for each character's role (e.g., library manager near library, students in classrooms)
6. "Currently" descriptions should be dynamic and reflect what the character might be doing at the start of the simulation

## Character Interaction Notes

Consider these potential interaction scenarios when generating agent definitions:

- **Teachers and Students**: Teachers interact with students in classrooms, provide guidance
- **Library Manager and Students**: Helps students find books, manages lending
- **Gym Manager and PE Teacher**: Coordinate sports activities, equipment usage
- **Cafeteria Manager and Everyone**: Provides meals, coordinates meal times
- **Security Guard and Everyone**: Monitors campus, manages entry/exit
- **Students with Each Other**: Study together, participate in activities, socialize
- **Counselor and Students**: Provides counseling, supports mental health
- **Principal and Staff**: Manages school, coordinates with teachers and staff

These interactions should be reflected in the characters' spatial memory trees and daily plans, allowing for natural social dynamics in the simulation.
