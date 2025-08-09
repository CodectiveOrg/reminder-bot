export class ReminderService {
  private readonly intervalDelay: number = 10_000;

  public run(): void {
    this.update();

    setInterval(() => {
      this.update();
    }, this.intervalDelay);
  }

  private update(): void {
    console.log("Updating...");
  }
}
