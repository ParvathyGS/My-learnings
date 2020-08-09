import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AnswersbymeComponent } from './answersbyme.component';

describe('AnswersbymeComponent', () => {
  let component: AnswersbymeComponent;
  let fixture: ComponentFixture<AnswersbymeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AnswersbymeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AnswersbymeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
