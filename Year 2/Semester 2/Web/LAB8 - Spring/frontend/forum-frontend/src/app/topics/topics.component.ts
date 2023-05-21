import {LiveAnnouncer} from '@angular/cdk/a11y';
import {AfterViewInit, Component, OnInit, ViewChild} from '@angular/core';
import {MatSort, Sort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import {MatPaginator} from "@angular/material/paginator";
import {TopicsService} from "../topics.service";
import {AuthService} from "../auth.service";
import {Router} from "@angular/router";
import {Topic} from "../Model/Topic";


@Component({
  selector: 'app-topics',
  templateUrl: './topics.component.html',
  styleUrls: ['./topics.component.css']
})
export class TopicsComponent implements OnInit {
  newTopicName: string = '';
  displayedColumns: string[] = ['id', 'name', 'created_by', 'action'];
  dataSource!: MatTableDataSource<Topic>;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private ApiSrv: TopicsService,
              private authSrv: AuthService,
              private router: Router) {
  }

  ngOnInit() {
    this.getTopicsList();
  }

  getTopicsList() {
    this.ApiSrv.getTopics().subscribe({
      next: (res) => {
        console.log(res);
        this.dataSource = new MatTableDataSource(res);
        this.dataSource.sort = this.sort;
        this.dataSource.paginator = this.paginator;
      },
      error: (err) => {
        console.log(err);
      }
    });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  deleteTopic(topicId: string) {
    this.ApiSrv.deleteTopic(topicId).subscribe({
      next: (res) => {
        this.getTopicsList();
      },
      error: console.log,
    });
  }

  onTopicNameChange(event: any) {
    this.newTopicName = event.target.value;
  }

  addTopic(): void {
    // Check if the new topic name is not empty
    console.log(this.newTopicName);
    if (this.newTopicName.trim() !== '') {
      const newTopic = {name: this.newTopicName, created_by: this.authSrv.getUsername()}; // Modify to include the 'created_by' field
      this.ApiSrv.createTopic(newTopic).subscribe(
        (response) => {
          // Handle successful addition of the topic
          console.log('Topic added successfully:', response);
          // Clear the input field and update the topic list if needed
          this.newTopicName = '';
          // Optionally, update the topic list to reflect the newly added topic
          this.getTopicsList();
        },
        (error) => {
          // Handle error
          console.error('Error adding topic:', error);
        }
      );
    }
  }

  TopicDetails(id: string): void{
    console.log(id);
    this.router.navigate(["/topic-details/",id]);
  }
}
