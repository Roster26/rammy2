import React, { Component } from 'react';
import { Storage } from '@google-cloud/storage';

class VideoUpload extends Component {
 constructor(props) {
    super(props);
    this.state = {
      videoFile: null,
    };
    this.onVideoChange = this.onVideoChange.bind(this);
    this.uploadVideo = this.uploadVideo.bind(this);
 }

 onVideoChange(e) {
    this.setState({ videoFile: e.target.files[0] });
 }

 async uploadVideo() {
    if (!this.state.videoFile) {
      alert('Please choose a video to upload.');
      return;
    }

    const storage = new Storage({
      keyFilename: 'path/to/your/keyfile.json',
      projectId: 'your-project-id',
    });

    const bucketName = 'your-bucket-name';
    const fileName = this.state.videoFile.name;

    const bucket = storage.bucket(bucketName);
    const file = bucket.file(fileName);

    const stream = file.createWriteStream({
      metadata: {
        contentType: this.state.videoFile.type,
      },
    });

    stream.on('error', (err) => {
      console.error('Error uploading video:', err);
    });

    stream.on('finish', () => {
      console.log('Video uploaded successfully.');
    });

    stream.end(this.state.videoFile);
 }

 render() {
    return (
      <div>
        <input type="file" accept="video/*" onChange={this.onVideoChange} />
        <button onClick={this.uploadVideo}>Upload Video</button>
      </div>
    );
 }
}

export default VideoUpload;