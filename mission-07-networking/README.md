# Mission 7 — How computers communicate

## 1. Task / objective
Understand foundational computer networking architectures, observe live network connectivity and DNS lookup tools from the terminal, analyze privacy-safe network diagnostics, and explain the step-by-step lifecycle of loading a website across client-server architectures.

---

## 2. Work completed
- Built a structured network concepts table defining LAN, MAN, WAN, DNS, Router, Protocol, Packet Switching, and Client-Server with real-world examples.
- Conducted terminal connectivity tests to a public website (`example.com`) using `ping` and captured round-trip packet latency and packet-loss statistics.
- Performed DNS resolution using `nslookup` to observe domain-to-IP address mapping (A records) while sanitizing local network identities.
- Formulated answers explaining connectivity diagnostics, DNS lookup outputs, and the browser resolution flow.
- Drafted a detailed 7-step explanation tracing how a client requests, routes, and renders a web page from a web server using standardized Internet protocols.

---

## 3. Commands / tools used
- `ping -c 4 example.com`: Sent four ICMP Echo Request packets to verify end-to-end network reachability, transmission latency, and packet loss.
- `nslookup example.com`: Queried the Domain Name System to inspect name resolution and IP address mapping.
- Terminal & Git: Used to record diagnostics, stage files, and synchronize with GitHub.

---

## 4. My understanding

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A high-speed network that interconnects computers and devices within a limited physical area, such as a home, classroom, or office building. | A home Wi-Fi network connecting a laptop, smartphone, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A larger network that spans an entire metropolitan area, city, or multi-building university campus, often bridging multiple LANs. | S-VYASA University campus fiber network interconnecting academic buildings, administrative blocks, and student hostels. |
| **WAN (Wide Area Network)** | A telecommunications network spanning large geographical regions, across states, countries, or globally. | The global Internet, connecting regional ISPs, data centers, and internet exchange points worldwide. |
| **DNS (Domain Name System)** | The distributed naming service that acts as the phonebook of the Internet, translating user-friendly domain names into machine-routable numerical IP addresses. | Resolving the domain name `example.com` into the IP address `172.66.147.243`. |
| **Router** | A networking device operating at the Network layer that inspects destination IP addresses on data packets and forwards them along the optimal path between different networks. | A home broadband router directing outbound web traffic from local Wi-Fi devices out through the ISP gateway. |
| **Protocol** | An established, formal set of standard rules that dictates how data is structured, transmitted, received, and error-checked across network communication channels. | **HTTPS** (Hypertext Transfer Protocol Secure) for encrypted web browsing, or **TCP** for reliable byte-stream transmission. |
| **Packet switching** | The network transmission method where digital messages are segmented into small, independent data chunks called packets, routed dynamically across varied network paths, and reassembled in order at the destination. | Streaming a YouTube video where audio and video chunks arrive as independent TCP/IP packets over different physical routes. |
| **Client-server** | A distributed computing architecture where client programs request resources or services, and centralized server programs process those requests and return responses. | Google Chrome web browser acting as the **client**, requesting a web page from GitHub's cloud web **server**. |

---

### Task 7.2 — Observe network information

#### Terminal Connectivity Test (`ping -c 4 example.com`)
```text
PING example.com (172.66.147.243): 56 data bytes
64 bytes from 172.66.147.243: icmp_seq=0 ttl=53 time=43.180 ms
64 bytes from 172.66.147.243: icmp_seq=1 ttl=53 time=79.483 ms
64 bytes from 172.66.147.243: icmp_seq=2 ttl=53 time=45.757 ms
64 bytes from 172.66.147.243: icmp_seq=3 ttl=53 time=51.741 ms

--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 43.180/55.040/79.483/14.450 ms
```

#### Terminal DNS Lookup (`nslookup example.com`)
```text
Server:		[redacted-local-dns-server]
Address:	[redacted]#53

Non-authoritative answer:
Name:	example.com
Address: 104.20.23.154
Name:	example.com
Address: 172.66.147.243
```

#### Analytical Answers
1. **What a connectivity test helps you check:**  
   A connectivity test (such as `ping`) verifies whether an end-to-end communication path exists between your local computer and a remote host. It indicates whether the remote server is active and reachable, measures latency (round-trip time in milliseconds), and checks for packet loss (instability in the network link).
2. **What information a DNS lookup displays:**  
   A DNS lookup displays the address of the resolver server that handled the query, whether the response was authoritative or cached (non-authoritative), and the resolved IPv4/IPv6 IP addresses corresponding to the queried domain name.
3. **The role of DNS when you enter a website name in a browser:**  
   Humans remember readable domain names (like `example.com`), but network routers and TCP/IP stacks only route packets using numerical IP addresses. When a user enters a URL, DNS translates that human-readable name into an IP address so the browser knows the exact destination server to connect to.

---

### Task 7.3 — What happens when you open a website?

A step-by-step trace of the communication lifecycle:

1. **Step 1 — User Input & URL Parsing:**  
   The user types a URL (e.g. `https://example.com`) into the web browser (**client**) address bar. The browser parses the URL into its components: protocol (`https`), domain name (`example.com`), and target path (`/`).
2. **Step 2 — DNS Resolution:**  
   The browser checks its local DNS cache. If the IP address is not cached, the client sends a recursive DNS lookup query through the local router to an upstream DNS recursive resolver. The **DNS** hierarchy resolves `example.com` to the server IP address `172.66.147.243` and returns it to the client.
3. **Step 3 — TCP Connection & TLS Handshake:**  
   The client initiates a connection with the server IP using the **TCP protocol** (Transmission Control Protocol) by performing a 3-way handshake (SYN, SYN-ACK, ACK). Because HTTPS is used, the client and server negotiate encryption keys through a TLS cryptographic handshake to establish a secure, encrypted session.
4. **Step 4 — Routing Packets Across the Network:**  
   The client formats an **HTTP GET** request. Operating system networking layers package this request into TCP segments and IP packets. Local **routers** and Internet Service Provider (ISP) gateway routers forward these packets across the Internet via packet switching until they arrive at the destination server.
5. **Step 5 — Server Processing:**  
   The web **server** receives the IP packets, reassembles them, inspects the HTTP GET request, locates the requested HTML file, and prepares an HTTP response status message (`200 OK`) accompanied by the web page payload.
6. **Step 6 — Response Transmission:**  
   The server transmits the HTTP response data back to the client as encrypted TCP/IP packets. Network routers direct the response packets back across the Internet to the client computer.
7. **Step 7 — Browser Rendering & Display:**  
   The client browser receives the response packets, reassembles the HTML content, parses the DOM tree, downloads linked style sheets and images, and renders the visual web page on screen for the user.

---

## 5. Difficulties faced
When inspecting `nslookup` output, the raw terminal display showed my local Wi-Fi router's private IPv6 address. I had to ensure that private network addresses and ISP identifiers were carefully sanitized before committing documentation.

## 6. How I resolved them
Replaced the local resolver IP and network identifiers with privacy-safe placeholders (`[redacted-local-dns-server]`) in compliance with the assignment privacy instructions.

---

## 7. Evidence / files
- `mission-07-networking/README.md`: Contains network definitions, live ping statistics, sanitized DNS lookup output, and the 7-step website loading walkthrough.

---

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Status: Staged and committed on `main`, pushed to GitHub remote `origin/main`.
