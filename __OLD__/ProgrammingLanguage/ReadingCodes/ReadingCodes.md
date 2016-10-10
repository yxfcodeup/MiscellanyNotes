# READING CODES
## C&C++
### Linux Kernel
*** 
#### Linux信号、信号处理和信号处理函数  
##### 描述
&emsp;&emsp;信号(signal)是一种软件中断，它提供了一种处理异步事件的方法，也是进程间惟一的异步通信方式。在Linux系统中，根据POSIX标准扩展以后的信号机制，不仅可以用来通知某种程序发生了什么事件，还可以给进程传递数据。  
* 信号来源  
信号的来源可以有很多种试，按照产生条件的不同可以分为硬件和软件两种。
    * 硬件方式  
    
    当用户在终端上按下某键时，将产生信号。如按下组合键后将产生一个SIGINT信号。  
    硬件异常产生信号：除数据、无效的存储访问等。这些事件通常由硬件(如:CPU)检测到，并将其通知给Linux操作系统内核，然后内核生成相应的信号，并把信号发送给该事件发生时正在进行的程序。
    
    * 软件方式
    
    用户在终端下调用kill命令向进程发送任务信号。  
    进程调用kill或sigqueue函数发送信号。  
    当检测到某种软件条件已经具备时发出信号，如由alarm或settimer设置的定时器超时时将生成SIGALRM信号。 
    
* 信号的种类  

    在Shell下输入kill –l 可显示Linux 系统支持的全部依赖，信号列表如下：
    ```
    1) SIGHUP          2) SIGINT           3) SIGQUIT        4) SIGILL
    5) SIGTRAP         6) SIGABRT          7) SIGBUS         8) SIGFPE
    9) SIGKILL         10) SIGUSR1         11) SIGSEGV       12) SIGUSR2
    13) SIGPIPE        14) SIGALRM         15) SIGTERM       16) SIGSTKFLT
    17) SIGCHLD        18) SIGCONT         19) SIGSTOP       20) SIGTSTP
    21) SIGTTIN        22) SIGTTOU         23) SIGURG        24) SIGXCPU
    25) SIGXFSZ        26) SIGVTALRM       27) SIGPROF       28) SIGWINCH
    29) SIGIO          30) SIGPWR          31) SIGSYS        34) SIGRTMIN
    35) SIGRTMIN+1     36) SIGRTMIN+2      37) SIGRTMIN+3    38) SIGRTMIN+4
    39) SIGRTMIN+5     40) SIGRTMIN+6      41) SIGRTMIN+7    42) SIGRTMIN+8
    43) SIGRTMIN+9     44) SIGRTMIN+10     45) SIGRTMIN+11   46) SIGRTMIN+12
    47) SIGRTMIN+13    48) SIGRTMIN+14     49) SIGRTMIN+15   50) SIGRTMAX-14
    51) SIGRTMAX-13    52) SIGRTMAX-12     53) SIGRTMAX-11   54) SIGRTMAX-10
    55) SIGRTMAX-9     56) SIGRTMAX-8      57) SIGRTMAX-7    58) SIGRTMAX-6
    59) SIGRTMAX-5     60) SIGRTMAX-4      61) SIGRTMAX-3    62) SIGRTMAX-2
    63) SIGRTMAX-1     64) SIGRTMAX   
    ```
    
    信号的值定义在signal.h中，在Linux中没有16和32这两个信号。上面信号的含义如下：
    ```
    (1) SIGHUP：当用户退出Shell时，由该Shell启的发所有进程都退接收到这个信号，默认动作为终止进程。
    (2) SIGINT：用户按下组合键时，用户端时向正在运行中的由该终端启动的程序发出此信号。默认动作为终止进程。
    (3) SIGQUIT：当用户按下组合键时产生该信号，用户终端向正在运行中的由该终端启动的程序发出此信号。默认动作为终止进程并产生core文件。
    (4) SIGILL ：CPU检测到某进程执行了非法指令。默认动作为终止进程并产生core文件。
    (5) SIGTRAP：该信号由断点指令或其他trap指令产生。默认动作为终止进程并产生core文件。
    (6) SIGABRT：调用abort函数时产生该信号。默认动作为终止进程并产生core文件。
    (7) SIGBUS：非法访问内存地址，包括内存地址对齐（alignment）出错，默认动作为终止进程并产生core文件。
    (8) SIGFPE：在发生致命的算术错误时产生。不仅包括浮点运行错误，还包括溢出及除数为0等所有的算术错误。默认动作为终止进程并产生core文件。
    (9) SIGKILL：无条件终止进程。本信号不能被忽略、处理和阻塞。默认动作为终止进程。它向系统管理员提供了一种可以杀死任何进程的方法。
    (10) SIGUSR1：用户定义的信号，即程序可以在程序中定义并使用该信号。默认动作为终止进程。
    (11) SIGSEGV：指示进程进行了无效的内存访问。默认动作为终止进程并使用该信号。默认动作为终止进程。
    (12) SIGUSR2：这是另外一个用户定义信号，程序员可以在程序中定义并使用该信号。默认动作为终止进程。
    (13) SIGPIPE：Broken pipe：向一个没有读端的管道写数据。默认动作为终止进程。
    (14) SIGALRM：定时器超时，超时的时间由系统调用alarm设置。默认动作为终止进程。
    (15) SIGTERM：程序结束(terminate)信号，与SIGKILL不同的是，该信号可以被阻塞和处理。通常用来要求程序正常退出。执行Shell命令kill时，缺少产生这个信号。默认动作为终止进程。
    (16) SIGCHLD：子程序结束时，父进程会收到这个信号。默认动作为忽略该信号。
    (17) SIGCONT：让一个暂停的进程继续执行。
    (18) SIGSTOP：停止(stopped)进程的执行。注意它和SIGTERM以及SIGINT的区别：该进程还未结束，只是暂停执行。本信号不能被忽略、处理和阻塞。默认作为暂停进程。
    (19) SIGTSTP：停止进程的动作，但该信号可以被处理和忽略。按下组合键时发出该信号。默认动作为暂停进程。
    (20) SIGTTIN：当后台进程要从用户终端读数据时，该终端中的所有进程会收到SIGTTIN信号。默认动作为暂停进程。
    (21) SIGTTOU：该信号类似于SIGTIN，在后台进程要向终端输出数据时产生。默认动作为暂停进程。
    (22) SIGURG：套接字（socket）上有紧急数据时，向当前正在运行的进程发出此信号，报告有紧急数据到达。默认动作为忽略该信号。
    (23) SIGXCPU：进程执行时间超过了分配给该进程的CPU时间，系统产生该信号并发送给该进程。默认动作为终止进程。
    (24) SIGXFSZ：超过文件最大长度的限制。默认动作为yl终止进程并产生core文件。
    (25) SIGVTALRM：虚拟时钟超时时产生该信号。类似于SIGALRM，但是它只计算该进程占有用的CPU时间。默认动作为终止进程。
    (26) SIGPROF：类似于SIGVTALRM，它不仅包括该进程占用的CPU时间还抱括执行系统调用的时间。默认动作为终止进程。
    (27) SIGWINCH：窗口大小改变时发出。默认动作为忽略该信号。
    (28) SIGIO：此信号向进程指示发出一个异步IO事件。默认动作为忽略。
    (29) SIGPWR：关机。默认动作为终止进程。
    (30) SIGRTMIN~SIGRTMAX：Linux的实时信号，它没有固定的含义(或者说可以由用户自由使用)。注意，Linux线程机制使用了前3个实时信号。所有的实时信号的默认动作都是终止进程。
```

    * 可靠信号与不可靠信号
    
    在Linux系统中，信号的可靠性是指信号是否会丢失，或者说该信号是否支持排除。SIGHUP( 1 ) ~ SIGSYS( 31 )之间的信号都是继承自UNIX系统是不可靠信号。Linux系统根据POSIX标准定义了SIGRTMIN(33) ~ SIGRTMAX(64)之间的信号，它们都是可靠信号，也称为实时信号。
    
    当导致产生信号的事件发生时，内核就产生一个信号。信号产生后，内核通常会在进程表中设置某种形的标志。当内核设置了这个标志，我们就说内核向一个进程递送了一个信号。信号产生(generate)和递送(delivery)之间的时间间隔，称主信号未决(pending)。
    
    进程可以调用sigpending将信号设为阻塞，如果为进程产生一个阻塞信号，而对信号的动作是捕捉该信号(即不忽略信号)，则内核将为该进程的此信号保持为未决状态，直到该进程对此信号解除阻塞或者对此信号的响应更改为忽略。如果在进程解除对某个信号的阻塞之前，这种信号发生了多次，那么如果信号被递送多次（即信号在未决信号队列里面排队），则称之为可靠信号；只被递送一次的信号称为不可靠信号。  
    
    * 信号的优先级  
    
    信号实质上是软中断，中断有优先级，信号也有优先级。如果一个进程有多个未决信号，则对于同一个未决的实时信号，内核将按照发送的顺序来递送信号。如果存在多个未决信号，则值（或者说编号）越小的越先被递送。如果即存在不可靠信号，又存在可靠信号（实时信号），虽然POSIX对这一情况没有明确规定，但Linux系统和大多数遵循POSIX标准的操作系统一样，将优先递送不可靠信号。
    
* 进程对信号的响应  

    当信号发生时，用户可以要求进程以下列3种方式之一对信号做出响应。  
    * 捕捉信号：对于要捕捉的信号，可以为其指定信号处理函数，信号发生时该函数自动被调用，在该函数内部实现对该信号的处理。  
    * 忽略信号：大多数信号都可使用这种方式进行处理，但是SIGKILL和SIGSTOP这两个信号不能被忽略，同时这两个信号也不能被捕获和阻塞。此外，如果忽略某某些由硬件异常产生的信号(如非法存储访问或除以0)，则进程的行为是不可预测的。
    * 按照系统默认方式处理。大部分信号的默认操作是终止进程，且所有的实时信号的默认动作都是终止进程。  

* 各种信号的默认处理情况  
    * 程序不可捕获、阻塞或忽略的信号有：SIGKILL,SIGSTOP  
    * 不能恢复至默认动作的信号有：SIGILL,SIGTRAP
    * 默认会导致进程流产的信号有：SIGABRT、SIGBUS、SIGFPE、SIGILL、SIGIOT、SIGQUIT、SIGSEGV、SIGTRAP、SIGXCPU、SIGXFSZ
    * 默认会导致进程退出的信号有：SIGALRM、SIGHUP、SIGINT、SIGKILL、SIGPIPE、SIGPOLL、SIGPROF、SIGSYS、SIGTERM、SIGUSR1、SIGUSR2、SIGVTALRM
    * 默认会导致进程停止的信号有：SIGSTOP、SIGTSTP、SIGTTIN、SIGTTOU
    * 默认进程忽略的信号有：SIGCHLD、SIGPWR、SIGURG、SIGWINCH
    
* 信号处理函数与相关结构  
    * 信号安装  
        * signal()  
        * sigaction()  
    * 发送信号函数  
        * int raise(int sig);  对当前进程发送指定信号
        * int pause(void);  将进程挂起等待信号
        * int kill(pid_t pid,int sig); 通过进程编号发送信号
        * unsigned int alarm(unsigned int seconds); 指定时间（秒）发送SIGALRM信号。 seconds 为0 时取消所有已设置的alarm请求；
        * int sigqueue(pid_t pid,int sig,const union sigval val);类似于kill函数，多了附带共用体 union sigval形数，将共用体中的成员 int sival_int 或 void *sival_ptr 的值传递给 信号处理函数中的定义类型 siginfo_t 中的 int si_int 或 void *si_ptr；
        * int setitimer(int which,const struct itimerval *value,struct itimerval *oldvalue);  可定时发送信号，根据which可指定三种信号类型：SIGALRM、SIGVTALRM 和 SIGPROF；作用时间也因which值不同而不同;struct itimerval 的成员 it_interval定义间隔时间，it_value 为0时，使计时器失效；
        * void abort(void) 将造成进程终止；除非捕获SIGABORT信号;
    * 信号集及信号集操作
        * sigfillset(sigset_t *set); 设置所有的信号到set信号集中；
        * sigemptyset(sigset_t *set); 从set信号集中清空所有信号；
        * sigaddset(sigset_t *set,int sig);在set信号集中加入sig信号；
        * sigdelset(sigset_t *set,int sig);在set信号集中删除sig信号；
    * 阻塞信号相关函数  
        * int sigprocmask(int how,const sigset_t *set,sigset_t *set);  根据how值，设置阻塞信号集，或释放阻塞的信号集
        * int sigpending(sigset_t *set); 获取在阻塞中的所有信号；
        * int sigsuspend(const sigset_t *set);    类似于 pause()函数！