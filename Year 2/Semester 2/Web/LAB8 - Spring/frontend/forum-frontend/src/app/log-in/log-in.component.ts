import {Component, OnInit} from '@angular/core';
import {AuthService} from "../auth.service";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent{
  loginForm: FormGroup;
  loading = false;
  submitted = false;
  error = '';

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  onSubmit() {
    this.submitted = true;

    // Stop here if form is invalid
    if (this.loginForm.invalid) {
      return;
    }

    this.loading = true;

    const { username, password } = this.loginForm.value;

    this.authService.login({ username, password }).subscribe(
      (response) => {
        // Check the response status code
        if (response === 'User signed-in successfully!.') {
          // Handle successful login
          this.loading = false;

          this.authService.setUsernameInSessionStorage(username); /// FCKING IMPORTANT !!!!!!!!!!!


          // Redirect or perform additional actions
          this.router.navigate(['/topics']);
        } else {
          // Handle other status codes
          this.loading = false;
          this.error = 'Login failed. Please try again.';
        }
      },
      (error) => {
        // Handle login error
        this.loading = false;
        this.error = error.message;
      }
    );
  }
}





