import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {SignUpDTO} from "./Model/SignUpDTO";
import {LogInDTO} from "./Model/LogInDTO";

@Injectable({
  providedIn: 'root'
})
export class AuthService {


  constructor(private http: HttpClient) { }

  baseUrl: string = 'http://127.0.0.1:5000/auth';

  register(user: SignUpDTO): Observable<any>{
    return this.http.post(this.baseUrl + '/signup', user) as Observable<any>;
  }

  login(user: LogInDTO): Observable<any>{
    const options = { responseType: 'text' as 'json' }; // Specify the responseType as 'text'
    return this.http.post(this.baseUrl + "/signin", user, options) as Observable<any>;
  }

  setUsernameInSessionStorage(username: string): void {
    sessionStorage.setItem('username', username);
  }

  getUsername(): string | null {
    const username = sessionStorage.getItem('username');
    console.log(sessionStorage);
    return username ? username : null;
  }
}
