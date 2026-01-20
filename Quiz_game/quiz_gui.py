import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QProgressBar, 
                             QFrame, QMessageBox)
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QFont, QColor, QIcon
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


class ModernQuizGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz Master")
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet(self.get_stylesheet())
        
        # Initialize quiz data
        question_bank = []
        for question in question_data:
            new_question = Question(question["question"], question["correct_answer"])
            question_bank.append(new_question)
        
        self.quiz = QuizBrain(question_bank)
        self.current_answer = None
        
        # Setup UI
        self.setup_ui()
        
        # Load first question
        if self.quiz.still_has_questions():
            self.load_next_question()
        else:
            self.show_quiz_complete()
    
    def setup_ui(self):
        """Setup the main UI components"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)
        
        # Header Section
        header_layout = QHBoxLayout()
        
        title_label = QLabel("Quiz Master")
        title_font = QFont("Segoe UI", 28, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #2c3e50;")
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        score_label_text = QLabel("Score:")
        score_label_text.setFont(QFont("Segoe UI", 12, QFont.Bold))
        header_layout.addWidget(score_label_text)
        
        self.score_label = QLabel("0/0")
        score_font = QFont("Segoe UI", 14, QFont.Bold)
        self.score_label.setFont(score_font)
        self.score_label.setStyleSheet("color: #27ae60; background-color: #ecf0f1; padding: 8px 16px; border-radius: 5px;")
        header_layout.addWidget(self.score_label)
        
        main_layout.addLayout(header_layout)
        
        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumHeight(10)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: none;
                background-color: #ecf0f1;
                border-radius: 5px;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                border-radius: 5px;
            }
        """)
        main_layout.addWidget(self.progress_bar)
        
        # Question Counter
        self.counter_label = QLabel("Question 1 of 10")
        self.counter_label.setFont(QFont("Segoe UI", 11))
        self.counter_label.setStyleSheet("color: #7f8c8d;")
        main_layout.addWidget(self.counter_label)
        
        # Question Display Area
        question_frame = QFrame()
        question_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border: 2px solid #ecf0f1;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        question_layout = QVBoxLayout(question_frame)
        question_layout.setContentsMargins(20, 20, 20, 20)
        
        self.question_label = QLabel()
        self.question_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.question_label.setStyleSheet("color: #2c3e50;")
        self.question_label.setWordWrap(True)
        self.question_label.setMinimumHeight(80)
        question_layout.addWidget(self.question_label)
        
        main_layout.addWidget(question_frame, 1)
        
        # Button Section
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        
        self.true_button = self.create_styled_button("✓ TRUE", "#27ae60", "#229954")
        self.true_button.clicked.connect(lambda: self.answer_question("True"))
        button_layout.addWidget(self.true_button)
        
        self.false_button = self.create_styled_button("✗ FALSE", "#e74c3c", "#c0392b")
        self.false_button.clicked.connect(lambda: self.answer_question("False"))
        button_layout.addWidget(self.false_button)
        
        main_layout.addLayout(button_layout)
        
        # Feedback Area
        self.feedback_label = QLabel()
        self.feedback_label.setFont(QFont("Segoe UI", 11))
        self.feedback_label.setAlignment(Qt.AlignCenter)
        self.feedback_label.setMinimumHeight(40)
        self.feedback_label.setWordWrap(True)
        main_layout.addWidget(self.feedback_label)
        
        # Next Button
        self.next_button = QPushButton("Next Question")
        self.next_button.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.next_button.setMinimumHeight(50)
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        self.next_button.clicked.connect(self.on_next_clicked)
        self.next_button.setEnabled(False)
        main_layout.addWidget(self.next_button)
    
    def create_styled_button(self, text, normal_color, hover_color):
        """Create a styled button with custom colors"""
        button = QPushButton(text)
        button.setFont(QFont("Segoe UI", 13, QFont.Bold))
        button.setMinimumHeight(60)
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {normal_color};
                color: white;
                border: none;
                border-radius: 8px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
            QPushButton:pressed {{
                background-color: {hover_color};
            }}
            QPushButton:disabled {{
                background-color: #bdc3c7;
                color: #95a5a6;
            }}
        """)
        return button
    
    def load_next_question(self):
        """Load the next question"""
        if self.quiz.still_has_questions():
            current_question = self.quiz.question_list[self.quiz.question_no]
            self.question_label.setText(current_question.text)
            self.current_answer = current_question.answer
            
            # Update counter and progress
            self.counter_label.setText(f"Question {self.quiz.question_no + 1} of {len(self.quiz.question_list)}")
            progress_value = int((self.quiz.question_no / len(self.quiz.question_list)) * 100)
            self.progress_bar.setValue(progress_value)
            
            # Reset UI
            self.true_button.setEnabled(True)
            self.false_button.setEnabled(True)
            self.next_button.setEnabled(False)
            self.feedback_label.setText("")
            self.feedback_label.setStyleSheet("color: #7f8c8d;")
        else:
            self.show_quiz_complete()
    
    def answer_question(self, user_answer):
        """Handle answer selection"""
        self.quiz.question_no += 1
        is_correct = user_answer.lower() == self.current_answer.lower()
        
        if is_correct:
            self.quiz.score += 1
            self.feedback_label.setText("✓ Correct!")
            self.feedback_label.setStyleSheet("color: #27ae60; font-weight: bold;")
        else:
            self.feedback_label.setText(f"✗ Wrong! The correct answer was: {self.current_answer}")
            self.feedback_label.setStyleSheet("color: #e74c3c; font-weight: bold;")
        
        # Update score display
        self.score_label.setText(f"{self.quiz.score}/{self.quiz.question_no}")
        
        # Disable answer buttons and enable next button
        self.true_button.setEnabled(False)
        self.false_button.setEnabled(False)
        self.next_button.setEnabled(True)
    
    def on_next_clicked(self):
        """Handle next button click"""
        if self.quiz.still_has_questions():
            self.load_next_question()
        else:
            self.show_quiz_complete()
    
    def show_quiz_complete(self):
        """Show completion message"""
        percentage = (self.quiz.score / len(self.quiz.question_list)) * 100
        
        title = "Quiz Complete!"
        message = f"""
Congratulations! You've completed the quiz.

Final Score: {self.quiz.score}/{len(self.quiz.question_list)}
Percentage: {percentage:.1f}%

{'Excellent work! 🎉' if percentage >= 80 else 'Good effort! 👍' if percentage >= 60 else 'Keep practicing! 💪'}
        """
        
        QMessageBox.information(self, title, message)
        self.close()
    
    def get_stylesheet(self):
        """Return the stylesheet for the application"""
        return """
            QMainWindow {
                background-color: #ffffff;
            }
            QLabel {
                color: #2c3e50;
            }
        """


def main():
    app = QApplication(sys.argv)
    window = ModernQuizGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
