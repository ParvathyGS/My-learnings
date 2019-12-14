import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


import { UserService } from '../user.service';
import { User } from '../user';
import { MessageService } from '../message.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})

export class SignupComponent implements OnInit {

  constructor(
    private userService: UserService,
    private router:Router,
    private messageService:MessageService,
  ) { }

  ngOnInit() {
    
  }
  
  onSubmit(user_details:User){

    this.userService.signupAction(user_details).subscribe(
      res => {  
          console.log(res.message);
          if (res.message == "Resgisteration successful") {
          this.messageService.add('Register Successful');
          this.router.navigateByUrl("/login");
        } else {
          console.log(res.message);
          this.messageService.add(res.message);
          this.router.navigateByUrl("/signup");
        }
      },
      );
  }
}
