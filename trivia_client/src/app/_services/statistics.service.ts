import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { Statistics} from "../_models/statistics";
import { AccountService } from "./account.service";
import { User } from "../_models/user";
import {environment} from "../../environments/environment";


@Injectable({ providedIn: 'root' })
export class StatisticsService {
  private statisticsSubject: BehaviorSubject<Statistics>;
  public statistics: Observable<Statistics>;

  constructor(
    private router: Router,
    private http: HttpClient,
    private accountService: AccountService
  ) {
    this.statistics = this._statistics(accountService.userValue.id)
    // @ts-ignore
    this.statisticsSubject = new BehaviorSubject<Statistics>(JSON.parse(localStorage.getItem('statistics')));
  }

  public getStatistics(): Statistics {
    return this.statisticsSubject.value
  }

  private _statistics(id: string) {
    return this.http.get<Statistics>(`${environment.microserviceUrl}/statistics/${id}/`,{ })
      .pipe(map(statistics => {
        localStorage.setItem('statistics', JSON.stringify(statistics));
        this.statisticsSubject.next(statistics);
        return statistics;
      }));
  }
}
