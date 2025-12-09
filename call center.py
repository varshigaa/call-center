#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct Call {
    int callID;
    char callerName[50];
    struct Call* next;
};


struct Agent {
    int agentID;
    int isAvailable;
    struct Agent* next;
};
struct Call* front = NULL;
struct Call* rear = NULL;


struct Agent* agentList = NULL;


void addCall(int id, char name[]) {
    struct Call* newCall = (struct Call*)malloc(sizeof(struct Call));
    newCall->callID = id;
    strcpy(newCall->callerName, name);
    newCall->next = NULL;

    if (rear == NULL) {
        front = rear = newCall;
    } else {
        rear->next = newCall;
        rear = newCall;
    }
    printf("Call from %s (ID: %d) added to the queue.\n", name, id);
}


void addAgent(int id) {
    struct Agent* newAgent = (struct Agent*)malloc(sizeof(struct Agent));
    newAgent->agentID = id;
    newAgent->isAvailable = 1; // Agent is available
    newAgent->next = agentList;
    agentList = newAgent;

    printf("Agent %d added to the system.\n", id);
}


void assignCall() {
    if (front == NULL) {
        printf("No calls in the queue.\n");
        return;
    }
    struct Agent* agent = agentList;
    while (agent != NULL) {
        if (agent->isAvailable) {
            // Assign the call to this agent
            printf("Assigning call from %s (ID: %d) to Agent %d.\n", front->callerName, front->callID, agent->agentID);
            agent->isAvailable = 0; // Mark agent as busy

            // Remove the call from the queue
            struct Call* temp = front;
            front = front->next;
            if (front == NULL) {
                rear = NULL;
            }
            free(temp);
            return;
        }
        agent = agent->next;
    }

    printf("No available agents to assign the call.\n");
}
void releaseAgent(int id) {
    struct Agent* agent = agentList;
    while (agent != NULL) {
        if (agent->agentID == id) {
            if (!agent->isAvailable) {
                agent->isAvailable = 1; // Mark agent as available
                printf("Agent %d is now available.\n", id);
            } else {
                printf("Agent %d is already available.\n", id);
            }
            return;
        }
        agent = agent->next;
    }
    printf("Agent %d not found.\n", id);
}
void displayCalls() {
    if (front == NULL) {
        printf("No calls waiting in the queue.\n");
        return;
    }

    struct Call* temp = front;
    printf("\nCurrent waiting calls:\n");
    while (temp != NULL) {
        printf("Caller: %s | Call ID: %d\n", temp->callerName, temp->callID);
        temp = temp->next;
    }
    printf("\n");
}
void displayAgents() {
    if (agentList == NULL) {
        printf("No agents available.\n");
        return;
    }

    struct Agent* temp = agentList;
    printf("\nAgent Status:\n");
    while (temp != NULL) {
        printf("Agent ID: %d | Status: %s\n", temp->agentID, temp->isAvailable ? "Available" : "Busy");
        temp = temp->next;
    }
    printf("\n");
}
int main() {
    int choice, id;
    char name[50];


    addAgent(1);
    addAgent(2);
    addAgent(3);

    while (1) {
        printf("\n*** Call Center Operation Menu ***\n");
        printf("1. Add New Call\n");
        printf("2. Assign Next Call to Available Agent\n");
        printf("3. Release Agent\n");
        printf("4. Display Waiting Calls\n");
        printf("5. Display Agent Status\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter Call ID: ");
                scanf("%d", &id);
                printf("Enter Caller Name: ");
                scanf("%s", name);
                addCall(id, name);
                break;

            case 2:
                assignCall();
                break;

            case 3:
                printf("Enter Agent ID to release: ");
                scanf("%d", &id);
                releaseAgent(id);
                break;

            case 4:
                displayCalls();
                break;

            case 5:
                displayAgents();
                break;

            case 6:
                printf("Exiting Call Center Simulation.\n");
                exit(0);

            default:
                printf("Invalid choice. Try again.\n");
        }
    }

    return 0;
}
