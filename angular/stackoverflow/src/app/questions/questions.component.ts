import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Question_details,Question } from '../question';
import { UserService } from '../user.service';
import { MessageService } from '../message.service';
import { QuestionsService } from '../questions.service';

@Component({
  selector: 'app-questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.css'],
})

export class QuestionsComponent implements OnInit {

  constructor(
    private userService:UserService,
    private route: ActivatedRoute,
    private messageService:MessageService,
    private questionService: QuestionsService,
  ) { }

  ngOnInit() {
    this.listQuestion();
  }


question_arr : Question_details[];

listQuestion() {
  this.userService.listallQuestion().subscribe(
    res => {
      this.question_arr = res,
      console.log(res);
    }
  );
}

}
