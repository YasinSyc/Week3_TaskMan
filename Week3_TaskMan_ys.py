#Once TaskManager sınıfını oluşturuyoruz. 
#işlemleri gerçekleştirmek için gerekli yöntemleri içerir.

class TaskManager:

   # __init__ yöntemi, sınıfın başlatıcı yöntemidir. 
   #Başlangıçta, tasks ve deleted_tasks adlı boş liste ve sözlük oluştururuz. 
   #sınıf içindeki tüm metotlar ilk parametre olarak self almalıdır. 
   #self, bir sınıf örneğini temsil eder ve bu örneğe erişim sağlar.
   
    def __init__(self):
        self.tasks = []
        self.deleted_tasks = {}

    #add_task yöntemi:Görev adını alır, ardından görevin otomatik sıra numarasını ve 
    #durumunu belirleyerek tasks listesine ekler.

    def add_task(self, task_name):
        # Tüm sıra numaralarını göz önünde bulundurarak bir benzersiz sıra numarası oluştur
        sequence_numbers = [task["Sequence Number"] for task in self.tasks] + list(self.deleted_tasks.keys())
        if sequence_numbers:
            next_sequence_number = max(sequence_numbers) + 1
        else:
            next_sequence_number = 1
    
        # Oluşturulan benzersiz sıra numarasıyla yeni görevi ekle
        self.tasks.append({"Sequence Number": next_sequence_number, "Task Name": task_name, "Status": "Pending"})
        print("Task added successfully.")


    #complete_task yöntemi: Belirtilen sıra numarasına sahip görevin durumunu "Completed" olarak günceller.

    def complete_task(self, sequence_number):
        for task in self.tasks:
            if task["Sequence Number"] == sequence_number:
                task["Status"] = "Completed"
                print("Task completed successfully.")
                return
        print("Task not found.")


    #delete_task yöntemi:Belirtilen sıra numarasına sahip görevi tasks listesinden kaldırır ve 
    #deleted_tasks sözlüğüne ekler.

    def delete_task(self, sequence_number):
        for task in self.tasks:
            if task["Sequence Number"] == sequence_number:
                self.deleted_tasks[sequence_number] = task
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")


    #list_completed_tasks yöntemi:tasks listesindeki görevler arasında dolaşır ve 
    #durumu "Completed" olanları listeler.   

    def list_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task["Status"] == "Completed"]
        if completed_tasks:
            print("Completed tasks:")
            for task in completed_tasks:
                print(task["Sequence Number"], "-", task["Task Name"])
        else:
            print("No completed tasks.")

    #list_all_tasks yöntemi: Görevleri sıra numaralarına göre sıralar ve 
    #her görevin sıra numarası, adı ve durumuyla birlikte listeler.

    def list_all_tasks(self):
        if self.tasks:
            sorted_tasks = sorted(self.tasks, key=lambda x: x["Sequence Number"])
            print("All tasks:")
            for task in sorted_tasks:
                print(task["Sequence Number"], "-", task["Task Name"], "-", task["Status"])
        else:
            print("No tasks added yet.")


    #exit_application yöntemi:Basit bir çıkış mesajı yazdırır ve 
    #exit() fonksiyonunu çağırarak programı sonlandırır.

    def exit_application(self):
        print("Exiting Task Manager Application.")
        exit()

#main fonksiyonu, kullanıcı arayüzünü yönetir. Bir döngü içinde menüyü gösterir, 
#kullanıcının seçimine göre ilgili yöntemi çağırır ve gerekli girişleri alır.

def main():
    task_manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Add a new task")
        print("2. Complete a task")
        print("3. Delete a task")
        print("4. List completed tasks")
        print("5. List all tasks with status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            task_manager.add_task(task_name)
        elif choice == "2":
            sequence_number = int(input("Enter the sequence number of the task to complete: "))
            task_manager.complete_task(sequence_number)
        elif choice == "3":
            sequence_number = int(input("Enter the sequence number of the task to delete: "))
            task_manager.delete_task(sequence_number)
        elif choice == "4":
            task_manager.list_completed_tasks()
        elif choice == "5":
            task_manager.list_all_tasks()
        elif choice == "6":
            task_manager.exit_application()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
