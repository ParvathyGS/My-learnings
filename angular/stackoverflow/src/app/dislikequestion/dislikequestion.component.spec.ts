import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DislikequestionComponent } from './dislikequestion.component';

describe('DislikequestionComponent', () => {
  let component: DislikequestionComponent;
  let fixture: ComponentFixture<DislikequestionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DislikequestionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DislikequestionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
