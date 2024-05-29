//========================================================================================================================================
// CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation	https://github.com/cyborg-ai-git // 
//========================================================================================================================================

using System.Collections;
using System;
using Evo;
//========================================================================================================================================
[System.Serializable]
public class EApiAudio : EObject
{
	
		 public Boolean isUrl;
		 public string name;
		 public string ext;
		 public Int64 length;
		 public byte[] data;

	override public void ToStream(System.IO.Stream stream)
	{
		base.ToStream(stream);
		
		this.DoWrite(this.isUrl, stream);
		this.DoWrite(this.name, stream);
		this.DoWrite(this.ext, stream);
		this.DoWrite(this.length, stream);
		this.DoWrite(this.data, stream);
	}

	override public void FromStream(System.IO.Stream stream)
	{
		base.FromStream(stream);
		
		this.isUrl = this.DoRead<Boolean>(stream);
		this.name = this.DoRead<string>(stream);
		this.ext = this.DoRead<string>(stream);
		this.length = this.DoRead<Int64>(stream);
		this.data = this.DoRead<byte[]>(stream);	
	}

	public override string ToString()
	{
		return base.ToString() + "\n"
			
				+ $"\tisUrl:{ this.isUrl }\n"
				+ $"\tname:{ this.name }\n"
				+ $"\text:{ this.ext }\n"
				+ $"\tlength:{ this.length }\n"
				+ $"\tdata:{ this.data }\n"
			;
	}
}