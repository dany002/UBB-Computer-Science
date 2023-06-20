import { Component } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  Roles: any = ['Admin', 'User'];
  registerForm: FormGroup;
  loading = false;
  submitted = false;
  error = '';

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService
  ) {
    this.registerForm = this.formBuilder.group({
      username: ['', Validators.required],
      name: ['', Validators.required],
      password: ['', Validators.required],
    });
  }


  onSubmit() {
    this.submitted = true;

    // Stop here if form is invalid
    if (this.registerForm.invalid) {
      return;
    }

    this.loading = true;

    const { username, name, password} = this.registerForm.value;

    this.authService.register({ username, name, password }).subscribe(
      () => {
        console.log("HI");
        // Handle successful registration
        this.loading = false;
        // Redirect or perform additional actions
      },
      (error) => {
        // Handle registration error
        this.loading = false;
        this.error = error.message;
      }
    );
  }
}
