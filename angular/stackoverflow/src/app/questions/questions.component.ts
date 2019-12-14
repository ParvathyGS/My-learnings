import { Component, OnInit } from '@angular/core';

import { Question } from '../question';
import { Question_details } from '../question';
import { UserService } from '../user.service';
import { LoginComponent } from '../login/login.component';

@Component({
  selector: 'app-questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.css'],
})

export class QuestionsComponent implements OnInit {

  constructor(
    private userService:UserService,
  ) { }

  ngOnInit() {
    this.listQuestion();
  }

  
question_arr : Question_details[];

listQuestion() {
  this.userService.listallQuestion().subscribe((res) => this.question_arr = res);
}
}
