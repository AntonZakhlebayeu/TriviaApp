import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { environment } from '@environments/environment';
import { User } from '../_models/user';

@Injectable({ providedIn: 'root' })
export class AccountService {
  private userSubject: BehaviorSubject<User>;
  public user: Observable<User>;

  constructor(
    private router: Router,
    private http: HttpClient
  ) {
    // @ts-ignore
    this.userSubject = new BehaviorSubject<User>(JSON.parse(localStorage.getItem('user')));
    this.user = this.userSubject.asObservable();
  }

  public get userValue(): User {
    return this.userSubject.value;
  }

  login(username: string, password: string) {
    return this.http.post<User>(`${environment.apiUrl}/users/login/`,
      { "user": { 'email': username, "password": password }})
      .pipe(map(user => {
        localStorage.setItem('user', JSON.stringify(user));
        this.userSubject.next(user);
        return user;
      }));
  }

  logout() {
    localStorage.removeItem('user');
    // @ts-ignore
    this.userSubject.next(null);
    this.router.navigate(['/account/login']);
  }

  register(user: User) {
    console.log({"user": { user }})
    return this.http.post(`${environment.apiUrl}/users/register/`, {"user": {
      'email': user.email, 'password': user.password, 'username': user.username,
        'first_name': user.firstName, 'last_name': user.lastName
      }});
  }

  getAll() {
    return this.http.get<User[]>(`${environment.apiUrl}/users/`);
  }

  getById(id: string) {
    return this.http.get<User>(`${environment.apiUrl}/users/${id}/`);
  }

  update(id: string, params: any) {
    return this.http.put(`${environment.apiUrl}/users/${id}/`, params)
      .pipe(map(x => {
        if (id == this.userValue.id) {
          const user = { ...this.userValue, ...params };
          localStorage.setItem('user', JSON.stringify(user));

          this.userSubject.next(user);
        }
        return x;
      }));
  }

  delete(id: string) {
    return this.http.delete(`${environment.apiUrl}/users/${id}/`)
      .pipe(map(x => {
        if (id == this.userValue.id) {
          this.logout();
        }
        return x;
      }));
  }
}
