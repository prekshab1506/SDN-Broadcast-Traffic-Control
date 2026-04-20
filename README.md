# SDN-Broadcast-Traffic-Control
Implementation of broadcast traffic control in Software Defined Networking (SDN) using POX controller and Mininet. Demonstrates how broadcast packets (ff:ff:ff:ff:ff:ff) can be detected and controlled to improve network efficiency.


SDN Broadcast Traffic Control using POX & Mininet

Overview  
This project demonstrates how Software Defined Networking (SDN) can be used to control broadcast traffic in a network. Using a custom POX controller, broadcast packets are detected and blocked to prevent unnecessary network flooding.

Objective  
- Understand broadcast behavior in networks  
- Implement a custom SDN controller  
- Control and reduce broadcast traffic  
- Analyze network performance before and after control  

Tools and Technologies  
- Mininet – Network emulation  
- POX Controller – SDN controller  
- OpenFlow – Communication protocol  
- Python – Controller implementation  

Key Concept  
- Broadcast MAC Address: ff:ff:ff:ff:ff:ff  
- Default behavior: Switch floods broadcast packets  
- Modified behavior: Controller detects and blocks broadcast traffic  

Working  

Before Control (Default Controller)  
- Controller: forwarding.l2_learning  
- Broadcast packets are flooded  
- ARP works normally  
- Hosts communicate successfully  

After Control (Custom Controller)  
- Controller: broadcast_control.py  
- Broadcast packets are detected and dropped  
- ARP fails (<incomplete>)  
- Communication is blocked  

Results  

Before Control  
- Ping successful  
- ARP table resolved  
- Bandwidth measurable using iperf  

After Control  
- Ping failed  
- ARP shows <incomplete>  
- Communication blocked due to broadcast control  

Bandwidth Analysis  
- Measured using iperf  
- High throughput observed in Mininet (virtual environment)  
- After applying control, bandwidth cannot be measured due to ARP failure  

Flow Table Analysis  
- Flow entries created during normal operation  
- Rules map input ports to output ports  
- After broadcast control, fewer or no flows are installed  

How to Run  

1. Start Default Controller  
cd ~/pox  
./pox.py forwarding.l2_learning  

2. Start Mininet  
sudo mn --topo single,3 --controller remote  

3. Test Network  
h1 ping h2  
h1 arp -a  

4. Run Bandwidth Test  
h2 iperf -s &  
h1 iperf -c h2  

5. Run Custom Controller  
./pox.py forwarding.broadcast_control  

6. Test After Control  
h1 ping h2  
h1 arp -a  

Screenshots  
Add screenshots of:  
- Before control (successful ping)  
- After control (failed ping)  
- ARP output  
- Flow table  
- iperf results  

Conclusion  
Broadcast traffic was successfully detected and controlled using an SDN-based approach. The experiment demonstrates how centralized control can reduce unnecessary network traffic and improve efficiency.

Future Improvements  
- Allow ARP while blocking other broadcast traffic  
- Implement rate limiting instead of complete blocking  
- Extend to larger network topologies  

Author  
- Your Name  

Key Feature  
Detects and blocks broadcast packets (ff:ff:ff:ff:ff:ff) using SDN controller logic.
