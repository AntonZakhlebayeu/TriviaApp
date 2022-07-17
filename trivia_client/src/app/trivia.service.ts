import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";

import { QuestionArray } from "./trivia";
import {environment} from "@environments/environment";


@Injectable({
 providedIn: 'root'
})
export class TriviaService {

 constructor(private http: HttpClient) { }

 getTrivia(): Observable<QuestionArray> {
   return this.http.get(`${environment.apiUrl}/questions/`) as Observable<QuestionArray>;
 }
}
