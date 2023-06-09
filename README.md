# Fastapi-Shakespeare


## Installation And Run Options


#### Option 1
> Note: You need to activate `git lfs` because the project contains large model files. Please make sure you have git lfs installed

```sh
git clone https://github.com/sfkara/Fastapi-shakespeare.git
cd Fastapi-shakespeare
git lfs pull
python3 -m env venv
source env/bin/activate
pip install -r requirements.txt
bash start.sh
```
#### Option 2
After clone and cd to the repo.
```sh
docker build -t  fastapi-shakespeare  .
docker run -p 8000:8000 fastapi-shakespeare
```
#### Option 3
App and model deployed on Amazon EC2 instance.You can reach the api via 
```sh
https://13.59.178.31:30724/generate_text
```
with valid POST request and body.

## Example Request And Response
After running the server, you can send input(json) with POST request.

Example Request:
```
{
  "input": "{YOUR_INPUT}"  
}
```
Example Response:
```
{
  "generated_text": "{GENERATED_TEXT_FROM_FINETUNED_MODEL}"  
}
```
![example](https://github.com/sfkara/Fastapi-shakespeare/assets/19964783/78e4ed99-cd17-420c-be7f-7f5668135a34)


 
## Software Design 
- After seeing the requirements, I first designed a simple API by getting a string from the uri with GET request.
(e.g 
```sh
GET 0.0.0.0:8000/generate_text/romeo
```
)
- Microservice : I changed it with POST request with a structure that takes input over json(for microservice structure). While setting up this structure, I paid attention to its modularity, I used pydantic for validation.
- In accordance with the Microservice architecture, it is possible to add more services to the structure in the future. (Models fine-tuned with other datasets, maybe like the image generation service)
- Temperature sampling and Encapsulation : Then, encapsulated the argument I gave in the Post request for temperature sampling, and I left this argument to the will. It stays in the service.py (temperature and max_length)(0.7 and 60).
It's entirely up to you whether you just give input as shown above, or use it in 3 arguments. 
- All this process can be seen from the commit history.
- Finally deployed model and app to Amazon EC2 instance(Amazon Linux 2023 AMI). After right configuration(instance type,architecture,volume and so on) api is reachable via public ip(https://13.59.178.31) and public IPV4 DNS(ec2-13-59-178-31.us-east-2.compute.amazonaws.com). I choosed AWS because I find it more scalable and managable rather than other cloud computing options.


## Finetune Process
 I used colab for finetuning. As can be seen in the notebook(Shakespeare.ipynb), I started with a standard pre-process after downloading the necessary library and dataset. I experimented with parameters such as optimizer, scheduler, batch size (to the extent allowed by colab free gpus) and various epochs.
  - CosineAnnealingLR(More reletable than other options, linear scheduler didn't give me the result I wanted(e.g average loss) )
  - Batch size(according to my experiments this was the biggest for this project)
  - Used Adam for optimizer(This was the safest for me)



 
